from flask import Flask, render_template
from auth_gmail import authenticate_gmail
import base64
import joblib

app = Flask(__name__)

# ✅ Load only the full pipeline model (which includes vectorizer)
with open('spam_model.pkl', 'rb') as f:
    model = joblib.load(f)

def get_email_text(payload):
    """Extract plain text from email payload"""
    if 'body' in payload and 'data' in payload['body']:
        return base64.urlsafe_b64decode(payload['body']['data']).decode('utf-8', errors='ignore')
    elif 'parts' in payload:
        for part in payload['parts']:
            if part.get('mimeType') == 'text/plain' and 'data' in part['body']:
                return base64.urlsafe_b64decode(part['body']['data']).decode('utf-8', errors='ignore')
    return ""

@app.route('/')
def index():
    service = authenticate_gmail()

    # Fetch 10 most recent emails
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
    messages = results.get('messages', [])

    output = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id'], format='full').execute()
        headers = msg_data['payload'].get('headers', [])
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')

        # Get email body text
        body_text = get_email_text(msg_data['payload'])

        # ✅ Just use the pipeline directly with raw text
        prediction = model.predict([body_text])[0]
        label = 'SPAM' if prediction == 1 else 'NOT SPAM'

        output.append({
            'subject': subject,
            'snippet': body_text[:200],
            'label': label
        })

    return render_template('index.html', emails=output)

if __name__ == '__main__':
    app.run(debug=True)

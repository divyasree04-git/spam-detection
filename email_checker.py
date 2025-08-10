from auth_gmail import authenticate_gmail
from spam_model import load_model # pyright: ignore[reportMissingImports]
import sqlite3
import time

def create_db():
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flagged_emails (
            id TEXT PRIMARY KEY,
            snippet TEXT,
            label TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_email_to_db(msg_id, snippet, label):
    conn = sqlite3.connect('emails.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO flagged_emails (id, snippet, label, timestamp)
        VALUES (?, ?, ?, datetime('now'))
    ''', (msg_id, snippet, label))
    conn.commit()
    conn.close()

def check_emails():
    print("[🔄] Checking new emails...")
    service = authenticate_gmail()
    model = load_model()

    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = msg_data.get('snippet', '')
        prediction = model.predict([snippet])[0]
        label = 'Spam' if prediction == 1 else 'Not Spam'

        save_email_to_db(msg['id'], snippet, label)
        print(f"✅ [{label}] {snippet[:80]}...")

create_db()

from auth_gmail import authenticate_gmail

def get_messages(service, max_results=10):
    results = service.users().messages().list(userId='me', maxResults=max_results).execute()
    messages = results.get('messages', [])
    
    emails = []
    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        snippet = txt.get('snippet')
        emails.append(snippet)
    return emails

if __name__ == "__main__":
    service = authenticate_gmail()
    emails = get_messages(service)
    for email in emails:
        print("✉️", email)

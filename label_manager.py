def add_label(service, msg_id, label_name='SPAM'):
    labels = service.users().labels().list(userId='me').execute()
    label_id = next((l['id'] for l in labels['labels'] if l['name'] == label_name), None)
    
    if label_id:
        service.users().messages().modify(
            userId='me',
            id=msg_id,
            body={'addLabelIds': [label_id]}
        ).execute()
# autodelete-e-mails
# to get all mails
# status, messages = imap.search(None, "ALL")
# to get mails by subject
# status, messages = imap.search(None, 'SUBJECT "Thanks for Subscribing to our Newsletter !"')
# to get mails after a specific date
# status, messages = imap.search(None, 'SINCE "01-JAN-2020"')
# to get mails before a specific date
# status, messages = imap.search(None, 'BEFORE "01-JAN-2020"')
# convert messages to a list of email IDs
To run this:

Change username and password for real email credentials, edit the imap.search() line for your use case and run delete_emails.py:
python delete_emails.py

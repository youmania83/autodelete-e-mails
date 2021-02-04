import imaplib
import email
from email.header import decode_header

# account credentials
username = "demo123@gmail.com"
password = "demo@123"
# create an IMAP4 class with SSL 
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)
imap.select("INBOX")
status, messages = imap.search(None, 'FROM "alerts@info.swiggy.in"')
messages = messages[0].split(b' ')
for mail in messages:
    _, msg = imap.fetch(mail, "(RFC822)")
    # you can delete the for loop for performance if you have a long list of emails
    # because it is only for printing the SUBJECT of target email to delete
    for response in msg:
        if isinstance(response, tuple):
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes type, decode to str
                subject = subject.decode()
            print("Deleting", subject)
    # mark the mail as deleted
    imap.store(mail, "+FLAGS", "\\Deleted")
    imap.expunge()
# close the mailbox
imap.close()
# logout from the account
imap.logout()
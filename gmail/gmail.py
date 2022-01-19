# Python 3.8.0
import smtplib
import imaplib
from email.header import decode_header
import email
import traceback

ORG_EMAIL = "@gmail.com"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
MAILS = []


def decode_mime_words(s):
    return u''.join(
        word.decode(encoding or 'utf8') if isinstance(
            word, bytes) else word
        for word, encoding in decode_header(s))


def getFlags(im, uid):
    return im.fetch(uid, '(FLAGS)')


def add_label(im, uid, flags):
    im.store(uid, '+FLAGS', '(%s)' % ' '.join(flags))


def rm_label(im, uid, flags):
    im.store(uid, '-FLAGS', '(%s)' % ' '.join(flags))


def move_to(im, uid, folder):
    result = im.copy(uid, folder)

    if result[0] == 'OK':
        delete(im, uid)


def archive(im, uid):
    move_to(im, uid, '"[Gmail]/All Mail"')


def delete(im, uid):
    flag = ['\\Deleted']
    add_label(im, uid, flag)


def read(im, uid):
    flags = ['\\Seen']
    add_label(im, uid, flags)


def unread(im, uid):
    flags = ['\\Seen']
    rm_label(im, uid, flags)


def parseBody(email):

    if email.get_content_maintype() == "multipart":
        for content in email.walk():
            if content.get_content_type() == "text/plain":
                body = content.get_payload(decode=True)
            elif content.get_content_type() == "text/html":
                html = content.get_payload(decode=True)
    elif email.get_content_maintype() == "text":
        body = email.get_payload()

    d = dict()
    d['text'] = body
    d['html'] = html

    return d


def connect(email, pwd):
    im = imaplib.IMAP4_SSL(SMTP_SERVER)
    im.login(email, pwd)

    return im


def disconnect(im):
    im.close
    im.logout()


def fetch(im, uid):
    return im.fetch(str(int(uid)), '(RFC822)')


def read_email_from_gmail(im, mailbox='INBOX', search='(UNSEEN)'):
    try:
        im.select(mailbox)

        response, mail_ids = im.search(
            None, search)

        if response == 'OK':
            return mail_ids
        else:
            return None

    except Exception as e:
        traceback.print_exc()
        print(str(e))


def getContent(arr):
    return email.message_from_string(str(arr[1], 'utf-8'))

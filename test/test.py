# -*- coding: utf-8 -*-

import re
import sys
import urllib.parse
import requests
import json
import gmail
import mysql.connector as mysql

if __name__ == "__main__":

    im = gmail.connect()
    mail_ids = gmail.read_email_from_gmail(
        im, "INBOX", '(FROM "test@adrii.com" UNSEEN)')

    for i in mail_ids[0].split():
        mail_data = gmail.fetch(im, i)

        for response_part in mail_data:
            arr = response_part[0]

            if isinstance(arr, tuple):
                msg = gmail.getContent(arr)

                email_subject = gmail.decode_mime_words(msg['subject'])
                email_from = gmail.decode_mime_words(msg['from'])
                email_to = gmail.decode_mime_words(msg['to'])
                email_body = gmail.parseBody(msg)
                body = str(email_body['text'])

                if "Lorem Ipsum" in body:
                    link = re.search(
                        "(?P<url>https?://[^\s]+)", body).group("url")
                    uri = urllib.parse.urlparse(link)
                    link = urllib.parse.unquote(link)

                    folder = 'Processed'
                    gmail.move_to(im, i, folder)
                    # gmail.read(im, i)
                    gmail.archive(im, i)

    gmail.disconnect(im)
    print("END")
    sys.exit()

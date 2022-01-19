# Gmail
Lightweight Python Gmail mail management library. Search, read, archive, mark as read/unread, delete emails, and manage labels. 

## Basic usage

To start, import the `gmail` library.
```python
import gmail
```  
## INIT
```python
im = gmail.connect($email, $pwd)
```

## SEARCH

```python
mail_ids = gmail.read_email_from_gmail(im, "INBOX", '(FROM "test@adrii.com" UNSEEN)')
```

## READ

```python
mail_ids = gmail.read_email_from_gmail(im, "INBOX", '(FROM "test@adrii.com" UNSEEN)')

for uid in mail_ids[0].split():
    mail_data = gmail.fetch(im, uid)

    for response_part in mail_data:
        arr = response_part[0]

        if isinstance(arr, tuple):
            msg = gmail.getContent(arr)

            email_subject = gmail.decode_mime_words(msg['subject'])
            email_from = gmail.decode_mime_words(msg['from'])
            email_to = gmail.decode_mime_words(msg['to'])
            email_body = gmail.parseBody(msg)
            body_txt = str(email_body['text'])
            body_html = str(email_body['html'])

            print("Subject: "+ email_subject + "\n")
            print("From: "+ email_from + "\n")
            print("To: "+ to + "\n")
            print("Body HTML: "+ body_html + "\n")
            print("Body TXT: "+ body_txt + "\n")

```

## ACTIONS

```python
gmail.read(im, uid)
email.unread(im, uid)

folder = 'Processed'
gmail.move_to(im, uid, folder)
gmail.archive(im, uid)

gmail.delete(im, uid)

flags = ["Processed", "foo", "var"]
gmail.add_label(im, uid, flags)

flags = ["Processed", "foo", "var"]
gmail.rm_label(im, uid, flags)

flags = gmail.getFlags(im, uid)
```

## FINISH
```python
gmail.disconnect(im)
```


# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# License
[MIT](https://github.com/AdrianVillamayor/Gmail/blob/master/LICENSE)

###Thanks for your help! 🎉

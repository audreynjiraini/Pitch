from flask_mail import Message
from flask import render_template
from . import mail

sender_email = 'audreywncode@gmail.com'
subject_pref = 'Welcome to Pitch Perfect'


def mail_message(subject, template, to, **kwargs):
    email = Message(subject_pref, sender = sender_email, recipients = [to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    mail.send(email)
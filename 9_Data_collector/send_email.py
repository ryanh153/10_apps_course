from email.mime.text import MIMEText
import smtplib


def send_email(email_ad, height, average_height, count):
    from_email = "ryan.h153@gmail.com"
    from_password = "Sl1pp3rystair"
    to_email = email_ad

    subject = "Height data"
    message = f'Your height is <strong>{height}</strong> cm.<br>' \
              f'The average height of the {count} users in the database is <strong>{average_height}</strong>.'

    msg = MIMEText(message, 'html')
    msg['subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)

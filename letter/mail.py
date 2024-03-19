import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_ya_mail(recipients_emails: list, msg_text: str, title:str):
    print(f"MSG TEXT: {msg_text}")
    login = 'doupig@yandex.ru'
    password = 'hyxhknnmooiykxms'

    msg = MIMEText(msg_text,'html')
    msg['Subject'] = Header(title, 'UTF-8')
    msg['From'] = login
    msg['To'] = ', '.join(recipients_emails)

    s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    except Exception as ex:
        print(ex, 'asdasd  ')
    finally:
        s.quit()

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(from_addr, to_addr, subject, password):
    msg = MIMEText("邮件正文",'html','utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.163.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())




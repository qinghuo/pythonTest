from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
class SendEmail:
 __slots__ = ('fromAddr','sdf')

 def __init__(self,fromAddr,password,toAddr):
    self.fromAddr=fromAddr
    self.password=password
    self.toAddr=toAddr
    self.smtpServer="smtp.163.com"
    self.smtpPort=465
    self.server = smtplib.SMTP_SSL(self.smtpServer,self.smtpPort)
    self.server.login(fromAddr, password)

 def __formatAddr(self,s):
         name, addr = parseaddr(s)
         return formataddr((Header(name, 'utf-8').encode(), addr))

 def send(self, theme, text):
     msg = MIMEText(text, 'plain', 'utf-8')
     msg['From'] = self.__formatAddr('taoqibao <%s>' % self.fromAddr)
     msg['To'] = self.__formatAddr('管理员 <%s>' % self.toAddr)
     msg['Subject'] = Header(theme, 'utf-8').encode()
     self.server.sendmail(self.fromAddr, [self.toAddr], msg.as_string())

 def quit(self):
     self.server.quit()

a=SendEmail(1,2,3)
a.test=1
a.quit()


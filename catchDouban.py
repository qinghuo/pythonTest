#-- coding:utf-8 --
import requests
import smtplib
from sendEmail3 import SendEmail
from lxml import html
cookie={}
raw_cookies='ll="118172"; bid=RJj1zMowuUs; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1515726455%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D6k-AsdBPNYVZmTvBoC7TVVufPQ4QrBz8a3FZuzciwGu%26wd%3D%26eqid%3D9af0870e0001286c000000045a582672%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.823320833.1515726456.1515726456.1515726456.1; __utmc=30149280; __utmz=30149280.1515726456.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; _ga=GA1.2.823320833.1515726456; _gid=GA1.2.1259779085.1515726471; push_doumail_num=0; __utmv=30149280.14896; __yadk_uid=1xRJ4VRRPPcMRpGTtMjzqzWzS1Nzjz7w; ap=1; push_noty_num=0; _pk_id.100001.8cb4=76daf53092b09542.1515726455.1.1515726532.1515726455.; __utmb=30149280.7.10.1515726456; _gat_UA-7019765-1=1; dbcl2="148962567:ET857fgrBFY"'
for line in raw_cookies.split(';'):
    key,value=line.split("=",1)
    cookie[key]=value

doubanPageUrl='https://www.douban.com/people/160427790/'
page=requests.get(doubanPageUrl,cookies=cookie)
tree = html.fromstring(page.text)

#XPath解析，获得你要的文字段落！
intro_raw = tree.xpath('//ul[@class="bs"]//a')

intro=[]
for i in intro_raw:
    intro.append(i.text)
my_sender = 'ma766722021@163.com'  # 发件人邮箱账号
my_pass = 'ma22021256'  # 发件人邮箱密码
my_user = '766722021@qq.com'  # 收件人邮箱账号，我这边发送给自己
sendEmailService=SendEmail(my_sender,my_pass,my_user)
sendEmailService.send("豆瓣",intro.__str__())
sendEmailService.quit()


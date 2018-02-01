#-- coding:utf-8 --
import requests
import socket
from lxml import html
import re
import time
import threading

headers = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
}

ipReg=r'((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))'
validIpList = []

def getProxyIpList():
    ipRep=requests.get('http://www.xicidaili.com/nn/',headers=headers);
    tree = html.fromstring(ipRep.text)
    trs=tree.xpath('//tr')
    httpsResult = []
    for tr in trs:
        ip=tr[1].text;
        if not re.match(ipReg,ip):
            continue
        protocol=tr[5].text
        if protocol!='HTTPS':
            continue
        port=tr[2].text

        httpsResult.append('https://'+ip+':'+port)
    return httpsResult

def getValidIpList():
    rawProxyIpList=getProxyIpList()
    threads = []
    for rawProxyIp in rawProxyIpList:
            threads.append(threading.Thread(target=validIp, args=(rawProxyIp,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return validIpList

def validIp(ip):
    try:
        rep=requests.get('https://www.weidai.com.cn', proxies={'https': ip}, timeout=4,headers=headers)
    except Exception as e:
        print('fail ' + ip)
    else:
        print('---------------------------success ' + ip)
        validIpList.append(ip)

if __name__ == "__main__":
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print(getValidIpList())
    with open('/Users/cengzhenmin/PycharmProjects/python/myTest/proxy/proxyIp.txt','w') as e:
        e.truncate()
        for ip in validIpList:
            e.write(ip+'\n')
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

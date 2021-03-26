import os
import shlex
import random
from IRC import *
from dcc import *

query = raw_input("Book title: ")

## IRC Config
server = "irc.irchighway.net"
port = 6667
channel = "#ebooks"
botnick = "bOOkbot"
irc = IRC()
irc.connect(server, port, channel, botnick)

irc.send("#ebooks", "@search " + query)

while True:
    text = irc.get_response()
    #if text.find('PRIVMSG') != -1: #see all messages, for fun
    #    print(text)
    if "DCC SEND" in text:
        print(text)
        break

dccString = text.split("DCC SEND ",1)[1].replace('\x01','')
dccString = shlex.split(dccString)

downloadfile(dccString)
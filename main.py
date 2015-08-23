import socket
import sys
import string

__VERSION__ = 0.1

#IRCBot 0.1
#Based in http://wiki.shellium.org/w/Writing_an_IRC_bot_in_Python

class IRCBot():
    #__init__ function
    def __init__(self, botnick, server, channel, port):
        self.botnick = botnick
        self.server = server
        self.channel = channel
        self.port = port
    
    #Encapsulation
    
    #Setters
    def set_botnick(self, botnick):
        self.botnick = botnick
    def set_server(self, server):
        self.server = server
    def set_channel(self, channel):
        self.channel = channel
    def set_port(self, port):
        self.port = port
        
    #Getters
    def get_botnick(self):
        return self.botnick
    def get_server(self):
        return self.server
    def get_channel(self):
        return self.channel
    def get_port(self):
        return self.port
    
    #Basic functions
    def ping(self): # Responds to server Pings.
        ircsock.send("PONG :Pong\n")  
    def sendmsg(self, channel, msg): # Sends messages to the channel
        ircsock.send("PRIVMSG "+ channel +" :"+ msg +"\n") 
    def joinchannel(self, channel): # Functions to join channels
        ircsock.send("JOIN "+ channel +"\n")
    
    #Configuration and channel connect
    def config(self):
        ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ircsock.connect((get_server(), get_port())) # Connects to the server
        ircsock.send("USER "+ get_botnick() +" "+ get_botnick() +" "+ get_botnick() +" :IRCBot 0.1") # user authentication
        ircsock.send("NICK "+ get_botnick() +"\n") # Assign the nick to the bot
        joinchannel(get_channel()) # Join the channel using the functions we previously defined
        while 1: # Be careful with these! it might send you to an infinite loop
            ircmsg = ircsock.recv(2048) # receive data from the server
            ircmsg = ircmsg.strip('\n\r') 
            print(ircmsg) 
            if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
              ping()

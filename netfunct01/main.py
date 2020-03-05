#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # device cmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... conecting with ' + coffeetime )
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )

# Start our main script
def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}
    print("Welcome to the network device command pusher") 
    print("\nData set found\n")
    commandpush(work2do)
main()

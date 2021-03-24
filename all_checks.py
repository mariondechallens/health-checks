#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coursera : Git and GitHub Course
"""
import os
import sys
import socket

def check_reboot():
    """Returns true if the computer has appending reboot."""
    
    return os.path.exists("/run/reboot-required")


def check_disk_full():
    
    return False


def check_root_full():
    """ Returns True if the root partition is full, False otherwise."""
    
    return check_disk_full()
    
def check_no_network():
    """ Returns True if it fails to resolve Google's URL, False otherwise."""    
    
    try :
        
        socket.gethostbyname('www.google.com')
        return False
    
    except :
        
        return True
        

def main():
    
    checks = [(check_reboot, "Pending reboot."),
              (check_root_full, "Root partition full."),
              (check_no_network, "No working network.")]
    
    everything_ok = True
    
    for check, msg in checks :
        if check():
            print(msg)
            everything_ok = False
    
    if not everything_ok :
        sys.exit(1)
        
    print('Everything is fine, that is good !')
    sys.exit(0)


main()

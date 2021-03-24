#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coursera : Git and GitHub Course
"""
import os
import sys

def check_reboot():
    """Returns true if the computer has appending reboot."""
    
    return os.path.exists("/run/reboot-required")


def check_disk_full():
    
    return True


def check_root_full():
    """ Returns True if the root partition is full, False otherwise"""
    
    return check_disk_full()
    
        

def main():
    
    checks = [(check_reboot, "Pending reboot."),
              (check_root_full, "Root partition full.")]
    
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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coursera : Git and GitHub Course - Week 1
"""
import os
import sys

def check_reboot():
    """Returns true if the computer has appending reboot."""
    
    return os.path.exists("/run/reboot-required")
    
def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)

    print('Everything is ok, that is good !')


main()

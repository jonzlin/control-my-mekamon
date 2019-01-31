#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
config.py
Configuration settings for Mekamon control
"""

__author__      = "Alex Watson"
__copyright__   = "Copyright 2019"

from collections import namedtuple

# Motion commands
Motion = namedtuple('Motion','cmd strafe fwd turn')

# BLE settings
message_delay = 0.5 # Time to sleep after sending message

# Server settings
# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
UDP_IP_ADDRESS = "192.168.4.2"
UDP_PORT_NO = 6789

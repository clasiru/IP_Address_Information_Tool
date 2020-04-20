#!/usr/bin/env python

#IP Address Information Tool (IPAIT)
#Author: Chandika Lasiru
#Blog: https://clasiru.blogspot.com

import socket;
import json;
from urllib.request import urlopen;

banner = """
 ██╗██████╗  █████╗ ██╗████████╗
 ██║██╔══██╗██╔══██╗██║╚══██╔══╝
 ██║██████╔╝███████║██║   ██║   
 ██║██╔═══╝ ██╔══██║██║   ██║   
 ██║██║     ██║  ██║██║   ██║   
 ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝    
     IP Address Information Tool
                  by Area Master

 Before using this Tool:-
   01. You must have Internet Connection.
   02. You must have to enter valid Public IP Address.
"""

print (banner, "\n");

def google_ok():
    try:
        urlopen('https://www.google.com', timeout=10);
        return True
    except: 
        return False
    return True

def yahoo_ok():
    try:
        urlopen('https://www.yahoo.com', timeout=10);
        return True
    except: 
        return False
    return True

def site_ok():
    try:
        urlopen('https://ipinfo.io', timeout=10);
        return True
    except: 
        return False
    return True

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address);
    except socket.error:
        return False
    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address);
    except socket.error:
        return False
    return True

host = input(" Enter IPv4 or IPv6 Address: ");

if google_ok() or yahoo_ok():
    if site_ok():
        if is_valid_ipv4_address(host) or is_valid_ipv6_address(host):

            whois = "https://ipinfo.io/" + host + "/json";
            data   = urlopen(whois).read();
            js = json.loads(data)

            if "bogon" in js :
                print ();
                print (" Error: Your IP Address is not a Public IP Address !");
        
            else:
                print ();
                print (" IP Address: " + js["ip"]);
                print (" Country: " + js["country"]);
                print (" Location: " + js["loc"]);
                print (" ASN/Organization: " + js["org"]);
                print (" Time Zone: " + js["timezone"]);
                #You can add additional lines here.
        else:
            print ();
            print (" Error: Your IP Address is not a Valid IP Address !");
    else:
        print ();
        print (" Error: Can't retrive Information !");
else:
    print ();
    print (" Error: Check your Internet Connection !");

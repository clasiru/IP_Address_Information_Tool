#!/usr/bin/env python

#IP Address Information Tool (IPAIT) v1.0
#Author: Area Master
#Website: Widane Forums
#Link: https://www.widane.com

import socket
import json;
from urllib.request import urlopen;

print ("  ___                  ___  ___          _            ");
print (" / _ \                 |  \/  |         | |           ");
print ("/ /_\ \_ __ ___  __ _  | .  . | __ _ ___| |_ ___ _ __ ");
print ("|  _  | '__/ _ \/ _` | | |\/| |/ _` / __| __/ _ \ '__|");
print ("| | | | | |  __/ (_| | | |  | | (_| \__ \ ||  __/ |   ");
print ("\_| |_/_|  \___|\__,_| \_|  |_/\__,_|___/\__\___|_|   ");
print ("                      IP Address Information Tool v1.0");
print ();
print ("Before using this Tool:-");
print ("01. You must have Internet Connection.");
print ("02. You must have to enter valid Public IP Address.");
print ();

def google_ok():
    try:
        urlopen('https://www.google.com', timeout=10)
        return True
    except: 
        return False
    return True

def yahoo_ok():
    try:
        urlopen('https://www.yahoo.com', timeout=10)
        return True
    except: 
        return False
    return True

def site_ok():
    try:
        urlopen('https://ipinfo.io', timeout=10)
        return True
    except: 
        return False
    return True

def is_valid_ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
    except socket.error:
        return False
    return True

def is_valid_ipv6_address(address):
    try:
        socket.inet_pton(socket.AF_INET6, address)
    except socket.error:
        return False
    return True

host = input("Enter IPv4 or IPv6 Address: ");

if google_ok() or yahoo_ok():
    if site_ok():
        if is_valid_ipv4_address(host) or is_valid_ipv6_address(host):

            whois = "https://ipinfo.io/" + host + "/json";
            data   = urlopen(whois).read();
            js = json.loads(data)

            if "bogon" in js :
                print ();
                print ("Error: Your IP Address is not a Public IP Address !");
        
            else:
                print ();
                print ("IP Address: " + js["ip"]);
                print ("Country: " + js["country"]);
                print ("Location: " + js["loc"]);
                print ("ASN/Organization: " + js["org"]);
                print ("Time Zone: " + js["timezone"]);
                #You can add additional lines here.
        else:
            print ();
            print ("Error: Your IP Address is not a Valid IP Address !");
    else:
        print ();
        print ("Error: Can't retrive Information !");
else:
    print ();
    print ("Error: Check your Internet Connection !");

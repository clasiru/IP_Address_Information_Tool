# IP Address Information Tool

Simple python script to view information about any IPv4 or IPv6 public IP address
-
This is the IP Address Information Tool (IPAIT). You need Python 3 and an Internet connection to run this tool. You can find information about any IPv4 or IPv6 Public IP Address. This tool can extract the following information.

01. Country
02. Location
03. ASN/Organization
04. Time Zone

Additionally, you can also obtain the following details by adding suitable lines into the ipait.py. (You can add additional lines after 84th line.)

01. Hostname -
```python
print ("Hostname: " + js["hostname"]);
```
02. City -
```python
print ("City: " + js["city"]);
```
03. Region -
```python
print ("Region: " + js["region"]);
```
04. Postal -
```python
print ("Postal: " + js["postal"]);
```


My blog post about this: [IP Address Information Tool (IPAIT)](https://clasiru.blogspot.com/2020/01/python-ip-address-information-tool-ipait.html)

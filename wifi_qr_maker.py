"""

share on twitter
share on facebook
share on Linkedin
share on Reddit
share on Hacker
Share
Creating 3D Printed WiFi Access QR Codes with Python
Eric J. Ma
Eric J. Ma
September 1, 2018
Summary

Over the weekend, I embarked on a project to create a 3D printed QR code that guests at our house could scan to gain access to our guest wireless network. Why 3D you might ask? Well, that’s how geeks like myself like to impress their guests! Also, let’s be real, I have a 3D printer at home, and I was looking for a fun way to put it to practical use. It turns out that it makes for some nice wall artwork as well.

In this first blog post I detail how I generate a QR code using Python, then how to build 3D printable blocks and, finally, how to convert that model into a file 3D printers can read.

In a follow-up blog post, I will specify how I created a hybrid command line app and Flask app from the same code base, using click and Flask. It will take the code that we write here and turn it into an app that can be used from the command line and from a web interface — it’s a great exercise in showing the similarities between the CLI and Flask. Coming soon!
Why a 3D QR code for my WIFI password?

There are a ton of QR code generators out there on the web and more than a handful of WiFi QR code generators too – so why did I embark on this project? Mainly, it was me wanting to scratch my itch surrounding QR codes. The last time I went to China (Xi’an and Shanghai, specifically), I saw QR codes everywhere. There surely had to be something good we could use this for at home that didn’t involve just packing and storage. Now that I know how simple it is to create a QR code using Python, I’m sure I’ll find myriad uses for them!
Getting Set Up

Ok, let’s get started! To create QR codes, you need to install pyqrcode and pypng in your environment:
pip install pyqrcode
pip install pypng


Let’s start by creating a QR code for our WiFi guest network.

Let’s say that these are the security credentials for the network:
SSID (a.k.a. Network Name): Family Guest Network
Password: vn8h2sncu093y3nd!
Security Type (one of WPA or WEP): WPA

QR codes are merely two-dimensional barcodes that encode a string that can be parsed by another program. In order to create a QR-code that is readable for accessing WiFi, we need a string that can be parsed by our devices. This string is structured as follows:
WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;

So in our case, we would want a string that looks like:
WIFI:S:Family Guest Network;T:WPA;P:vn8h2sncu093y3nd!;;

Now, we can code up our Python program to encode the QR code for us. I’ll assume you’re running Python 3.6 or later."""


import pyqrcode as pq

ssid = "Airtel-E5573-5FE7"
security = "WPA2"
password = "ahnh1305"
qr = pq.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
"""module_color="#eee"""
qr.png('wifi9.png' , scale = 5  )#background="#36C") ## adding colours must add hexadecimal values scale is for setting the size
#qr.png('wifi.png' , scale = 5) # scale is the size of the qrcode

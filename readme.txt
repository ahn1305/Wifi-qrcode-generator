Let’s start by creating a QR code for our WiFi guest network.

Let’s say that these are the security credentials for the network:

SSID (a.k.a. Network Name): Family Guest Network
Password: vn8h2sncu093y3nd!
Security Type (one of WPA or WEP): WPA

QR codes are merely two-dimensional barcodes that encode a string that can be parsed by another program.

 In order to create a QR-code that is readable for accessing WiFi, we need a string that can be parsed by our devices. This string is structured as follows:

WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;

So in our case, we would want a string that looks like:

WIFI:S:Family Guest Network;T:WPA;P:vn8h2sncu093y3nd!;;

Now, we can code up our Python program to encode the QR code for us. I’ll assume you’re running Python 3.6 or later."""


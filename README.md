# Intersight Dump NFNIC Driver Inventory

Example: Use API to dump all in use NFNIC driver versions and associated serial numbers


Pre-reqs:
-Intersight API Keys

-Python 3.x

-Intersight Advantages licenses for HCL feature


Usage:
Modify api_key_id in incompatibledrivers.py to your API public key

Modify SecretKey.txt to your API private key



Example Output:
#python nfnic-inventory.py

#4.0.0.24-1OEM.670.0.0.8169922 nfnic FCH12345 UCSB-B200-M5

#4.0.0.35-1OEM.670.0.0.8169922 nfnic FCH67890 UCSB-B200-M4

#4.0.0.40-1OEM.670.0.0.8169922 nfnic FCH34567 UCSB-B200-M4

#4.0.0.40-1OEM.670.0.0.8169922 nfnic FCH65432 UCSB-B200-M4

#4.0.0.70-1OEM.670.0.0.8169922 nfnic FCH23456 UCSB-B200-M4

#4.0.0.35-1OEM.670.0.0.8169922 nfnic FCH98765 UCSB-B200-M3

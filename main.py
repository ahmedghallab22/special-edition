import wmi
c=wmi.WMI()
serial = c.Win32_BaseBoard()[0].SerialNumber.strip()
if (serial=="Default string"):
    print("my_code")
else:
    print("You are not authorized to use the program. Contact the owner of the program on WhatsApp: 01207059498")








# Wmic BaseBoard get serialnumber

import os


ssid = "wifi name" # "python_wifi"
password = "wifi password" # "pysecret_psswd@n"


os.system(f"nmcli d wifi connect '{ssid}' password '{password}'")

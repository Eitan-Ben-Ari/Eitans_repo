from regular_extentions1 import data_dict
import re
pattern = r"\b\d{1,3}(\.\d{1,3}){3}\b"
matches = re.findall(pattern, "".join(data_dict["ip_addresses"]))
print("IP Addresses:", matches)
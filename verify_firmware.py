import json
import os
import re

with open('firmware-index.json', 'r') as f:
    firmware_files = json.load(f)

all_firmwares_in_index = [a for (_, major_vers) in firmware_files["Releases"].items() 
                            for (_, vers_cont) in major_vers.items() 
                            for dev_entry in vers_cont 
                            for a in dev_entry['AvailRelease']]
all_firmwares_in_directory = os.listdir('ctr-device-firmware')

items_missing_from_directory = list(set(all_firmwares_in_index).difference(all_firmwares_in_directory))
if len(items_missing_from_directory) != 0:
    raise Exception(f'The following firmwares are not present in the directory: {items_missing_from_directory}')

# We don't care about any firmwares that are in the directory that aren't present in the index
# items_missing_from_index = list(set(all_firmwares_in_directory).difference(all_firmwares_in_index))
# if len(items_missing_from_index) != 0:
#     raise Exception(f'The following firmwares are not present in the index: {items_missing_from_index}')


dev_entry = [a for (_, major_vers) in firmware_files["Releases"].items() 
               for (_, vers_cont) in major_vers.items() 
               for a in vers_cont]

version_regex = r'([0-9]+)\.([0-9]+)(\.([0-9]+)\.([0-9]+))?'

for d in dev_entry:
    if d["LatestRelease"] != d["AvailRelease"][0]:
        raise Exception(f"Device {d['Device']} does not have latest release matching first avail release")
    

    latest_vers_num_regex = re.search(version_regex, d["LatestRelease"])
    latest_vers = latest_vers_num_regex.group(0)

    if latest_vers != d["LatestVersion"]:
        raise Exception(f"Device {d['Device']} does not match latest version")

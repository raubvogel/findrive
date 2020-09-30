#! /usr/bin/env python
""" Scan computer for hard drives and list useful properties

Output
------
List of hard drives, including
- device name (as in /dev/devname)
- PCI path (/sys/bus/pci/devices/pcipath)
- vendor+device info

Notes
-----
1: This started as a quick program to look for NVMe hard drives and
   return their PCI path, dev path, vendor, and device info.

Naming Convention
-----------------
camelCase                  : variables
lower_case_with_underscore : functions

Attributes
----------
For the device '/sys/bus/pci/devices/0000:67:00.0/nvme/nvme7/nvme6n1'
pcipath : [5] = 0000:67:00.0
devname : [8] = nvme6n1
vendor and device: we have to get it by other means
"""

import glob
import os
import random
import getopt

def read_file(fn):
    with open(fn) as f:
        file_contents = f.read()
        # f.close()
        return file_contents

def create_dev_list(devPath, devOrder):
    devList = []
    type(devList)

    def get_dev_info( devDir ):
        devInfo = {}

        devInfo[ 'pcipath' ] = devDir.split('/')[5]
        devInfo[ 'devname' ] = devDir.split('/')[8]
        devInfo[ 'vendor+device' ] = read_file('/sys/bus/pci/devices/' + \
                devInfo['pcipath'] + \
                '/uevent').strip().split("\n")[2].split("=")[1]
        return( devInfo)

    for dirPath in glob.glob(devPath):
        devLength = len(devList)
        if (devLength != 0):
            devList.insert(random.randrange(devLength), get_dev_info(dirPath))
        else:
            devList.append(get_dev_info(dirPath))

        if (devOrder != "random"):
            tempList = sorted(devList, key=lambda x : x['devname'])
            devList = tempList

    return devList

myPath = "/sys/bus/pci/devices/*/nvme/nvme?/nvme*"
devList = create_dev_list( myPath, "random" )
for devItem in devList:
    print( devItem )

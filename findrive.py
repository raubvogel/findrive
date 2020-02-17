#! /usr/bin/env python
""" Scan computer for hard drives and list useful properties

Notes
-----
1: This started as a quick program to look for NVMe hard drives and 
   return their PCI path, dev path, vendor, and device info.

Attributes
----------
For the device '/sys/bus/pci/devices/0000:67:00.0/nvme/nvme7/nvme6n1'
pcipath : [5] = 0000:67:00.0
devname : [8] = nvme6n1
vendor and device: we have to get it by other means
"""

import glob
import os

devinfo = {}

def read_file(fn):
    with open(fn) as f:
        file_contents = f.read()
        # f.close()
        return file_contents

mypath = "/sys/bus/pci/devices/*/nvme/nvme?/nvme*"
for dirpath in glob.glob(mypath):
    devinfo[ 'pcipath'] = dirpath.split('/')[5]
    devinfo['devname' ] = dirpath.split('/')[8]
    devinfo[ 'vendor+device' ] = read_file('/sys/bus/pci/devices/' + devinfo['pcipath'] + '/uevent').strip().split("\n")[2].split("=")[1]
    print( devinfo)

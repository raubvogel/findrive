# findrive
Script to find all hard drives in a computer

## Note

I will be using this script as an excuse to learn how to properly document 
Python code. You have been warned!

## History

This script started life as a way for me to list the NVMe hard drives 
attached to a given host. As if now, output looks like this

``` bash
[root@testbox ~]# ./findrive.py
{'pcipath': '0000:67:00.0', 'devname': 'nvme6n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:60:00.0', 'devname': 'nvme0n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:66:00.0', 'devname': 'nvme2n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:65:00.0', 'devname': 'nvme4n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:64:00.0', 'devname': 'nvme5n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:63:00.0', 'devname': 'nvme3n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:69:00.0', 'devname': 'nvme8n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:62:00.0', 'devname': 'nvme7n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:68:00.0', 'devname': 'nvme1n1', 'vendor+device': '8086:0A54'}
{'pcipath': '0000:61:00.0', 'devname': 'nvme9n1', 'vendor+device': '8086:0A54'}
[root@testbox ~]#
```

(yes I renamed it) because I wanted to be able to import the results as a
list of dictionaries in python so I can do things like loop over that list
or search for a specific one; just because all the drives in the above sample
output have the same vendor and device ID does not mean it only looks for those
specific drives. In fact, if it is a NVMe hard drive, it is fair game. With 
that said, there is nothing stopping you from converting it into a comma separated list:

``` bash
[root@testbox tests]# ~/findrive.py | cut -d \' -f4,8,12|tr \' \,
0000:67:00.0,nvme2n1,8086:0A54
0000:60:00.0,nvme6n1,8086:0A54
0000:66:00.0,nvme0n1,8086:0A54
0000:65:00.0,nvme4n1,8086:0A54
0000:64:00.0,nvme5n1,8086:0A54
0000:69:00.0,nvme9n1,8086:0A54
0000:62:00.0,nvme1n1,8086:0A54
0000:68:00.0,nvme8n1,8086:0A54
0000:61:00.0,nvme3n1,8086:0A54
[root@testbox tests]#
```

Goal is to expand it to cover other hard drives, hence the new name. Wishful
thinking? Time will tell...

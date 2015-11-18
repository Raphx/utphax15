#!/usr/bin/env python

import requests

url = 'http://mawar.utphax.my/1f0f5d639c27a06467df0f96f4e0a9f8ac99f6b1'
params = {'cubaan': '', 'filename': 'aaa.txt'}
r = requests.get(url, params=params)

print r.headers
print r.content
#!/usr/bin/env python3

import sys
import json
import os.path
from urllib.request import urlretrieve

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 1e2 / totalsize
        s = "\r%5.1f%% %*d / %d" % (
            percent, len(str(totalsize)), readsofar, totalsize)
        sys.stderr.write(s)
        if readsofar >= totalsize: # near the end

            sys.stderr.write("\n")
    else: # total size is unknown

        sys.stderr.write("read %d\n" % (readsofar,))

with open("urlist.json", "r") as docset_json :
    docset_list = json.load(docset_json)

    for docset in docset_list:
        print(docset["url"])

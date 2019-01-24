import os
import sys
import yaml
import requests as re

URL = "https://api.dlercloud.com/link/8kyigPBojXY88d3q?is_mu=0&clash=1"
PATH = "/home/viewv/.config/clash/"
NAME = "config.yml"

print("Welcome to Fetch!")

with open(PATH + NAME, "wb") as f:
    print("Downloading Config File")
    res = re.get(URL, stream=True)
    total_length = res.headers.get('content-length')

    if total_length is None:  # no content length header
        f.write(res.content)
    else:
        dl = 0
        total_length = int(total_length)
        for data in res.iter_content(chunk_size=4096):
            dl += len(data)
            f.write(data)
            done = int(50 * dl / total_length)
            sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)))
            sys.stdout.flush()

with open(PATH + NAME, "w+") as f:
    config = f.read()
    dict = yaml.load(config)
    dict['external-controller'] = "127.0.0.1:1234"
    yaml.dump(dict, f)

os.system('pm2 restart clash-linux')

print("Finish")

import os
import yaml
import requests

URL = "https://api.dlercloud.com/link/8kyigPBojXY88d3q?is_mu=0&clash=1"
PATH = "/home/viewv/.config/clash/"
NAME = "config.yml"

print("Welcome to Fetch!")

r = requests.get(URL)

with open(PATH + NAME, 'wb') as f:
    f.write(r.content)

with open(PATH + NAME, 'r+') as f:
    config = yaml.load(f)
    print(config)
    config['external-controller'] = "127.0.0.1:1234"
    yaml.dump(config, f)

os.system('pm2 restart clash-linux')

print("Finish")

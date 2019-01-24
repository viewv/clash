import os
import requests
from ruamel import yaml
from tqdm import tqdm

URL = "Your Url"
PATH = "Your Config Path"
NAME = "config.yml"
IPHOST = "127.0.0.1:1234"  # external-controller

print(
    """
                                                   
  ,ad8888ba,  88                      88           
 d8"'    `"8b 88                      88           
d8'           88                      88           
88            88 ,adPPYYba, ,adPPYba, 88,dPPYba,   
88            88 ""     `Y8 I8[    "" 88P'    "8a  
Y8,           88 ,adPPPPP88  `"Y8ba,  88       88  
 Y8a.    .a8P 88 88,    ,88 aa    ]8I 88       88  
  `"Y8888Y"'  88 `"8bbdP"Y8 `"YbbdP"' 88       88  
                                                   
                                                   
                                                                              
88        88                      88                                          
88        88                      88              ,d                          
88        88                      88              88                          
88        88 8b,dPPYba,   ,adPPYb,88 ,adPPYYba, MM88MMM ,adPPYba, 8b,dPPYba,  
88        88 88P'    "8a a8"    `Y88 ""     `Y8   88   a8P_____88 88P'   "Y8  
88        88 88       d8 8b       88 ,adPPPPP88   88   8PP""""""" 88          
Y8a.    .a8P 88b,   ,a8" "8a,   ,d88 88,    ,88   88,  "8b,   ,aa 88          
 `"Y8888Y"'  88`YbbdP"'   `"8bbdP"Y8 `"8bbdP"Y8   "Y888 `"Ybbd8"' 88          
             88                                                               
             88                                                               
                                                           
"""
)
print("Welcome to Clash Auto-Updater!")

r = requests.get(url=URL, stream=True)
content_size = int(r.headers['Content-Length']) / 1024

with open(PATH + NAME, 'wb') as f:
    print("Size: ", content_size, 'k, Start Downloading...')
    for data in tqdm(iterable=r.iter_content(512), total=content_size, unit='k', desc=NAME):
        f.write(data)
    print(NAME + ": All Done!")

with open(PATH + NAME, 'r+') as f:
    config = yaml.load(f, Loader=yaml.RoundTripLoader)
    config['external-controller'] = IPHOST
with open(PATH + NAME, 'w') as nf:
    yaml.dump(config, nf, Dumper=yaml.RoundTripDumper)

os.system('pm2 restart clash-linux')

print("Finish!")

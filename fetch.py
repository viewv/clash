import os
import yaml
import requests
from tqdm import tqdm

URL = "https://api.dlercloud.com/link/8kyigPBojXY88d3q?is_mu=0&clash=1"
PATH = "/home/viewv/.config/clash/"
NAME = "config.yml"
IPHOST = "127.0.0.1:1234"

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
88        88 88P'    "8a a8"    `Y88 ""     `Y8   88   a8P     88 88P'   "Y8  
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
    print("Size:", content_size, 'k, Start Downloading...')
    for data in tqdm(iterable=r.iter_content(128), total=content_size, unit='k', desc=NAME):
        f.write(data)
    print(NAME + "All Done!")

with open(PATH + NAME, 'r+') as f:
    config = yaml.load(f)
    config['external-controller'] = IPHOST
    yaml.dump(config, f)

os.system('pm2 restart clash-linux')

print("Finish")

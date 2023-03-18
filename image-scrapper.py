import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from tqdm import tqdm

link = input("Enter link:")
txt = requests.get(link).text
soup = BeautifulSoup(txt, 'html.parser')
img_elems = soup.find_all('img')

path = "images/"
if not os.path.exists(path):
    os.makedirs(path)
img_list = [img_elem.attrs['src'] for img_elem in img_elems]
# loop = len(img)
i=1
for img in tqdm(img_list):
    try:
        file_path = Path(path + str(i).zfill(2) + ".png")
        R = requests.get(link+img)
    except:
        print("Exception: "+img)
        continue
    if R.status_code != 200:
        print("Error: "+img)
        continue
	#time.sleep(1)
    try:
        file_path.write_bytes(R.content)
    except:
        print("Cannot write image: "+img)
        continue
print(f"Done!")
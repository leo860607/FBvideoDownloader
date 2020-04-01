#refer from https://itrendbuzz.com/download-facebook-videos/
import sys
import os
import re
import requests as r
import wget
import pathlib
import urllib.request as ulib
from tqdm import tqdm
from DraculaPlugin import *
DraculaLinStamp()
filedir = pathlib.Path(__file__).parent.absolute()

ERASE_LINE = '\033[K'
## Download Low Resolution Video
tempdata=0
def progress_function(blocks, block_size, total_size):
    global tempdata
    global pbar
    pbar.total=total_size
    progress=blocks*block_size-tempdata
    pbar.update(progress)
    tempdata=blocks*block_size
    #print("tempdata= "+str(tempdata))

try:
    LINK = input("Enter a Facebook Video Post URL: ")
    ffilename=input("Filename: ")
    vquality=input("Quality(1.High/2.Normal): ")
    html = r.get(LINK)
    #print(html.text)
    if vquality==1:
        sdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
    else :
        sdvideo_url = re.search('sd_src:"(.+?)"', html.text)[1]
except r.ConnectionError as e:
    print("OOPS!! Connection Error.")
except r.Timeout as e:
    print("OOPS!! Timeout Error")
except r.RequestException as e:
    print("OOPS!! General Error or Invalid URL")
except (KeyboardInterrupt, SystemExit):
    print("Ok ok, quitting")
    sys.exit(1)
except TypeError:
    print("Video May Private or Invalid URL")
else:
    if vquality==1:
        sd_url = sdvideo_url.replace('hd_src:"', '')   
        print("\n")
        print("HIGH Quality: " + sd_url)
    else :
        sd_url = sdvideo_url.replace('sd_src:"', '')
        print("\n")
        print("Normal Quality: " + sd_url)
    print("[+] Video Started Downloading")
    pbar=tqdm(position=0, leave=True,ascii = True)
    with pbar:
        ulib.urlretrieve(sd_url,ffilename+".mp4", progress_function)
    pbar.close()

#this method can work
    #video = r.get(sd_url).content
    #with open(ffilename+".mp4", 'wb') as handler:
    #    handler.write(video)
#this method can work2, but i need a more flexible progressbar for gui designment
    #tfilename=wget.download(sd_url,os.path.join(filedir,""))
    #os.rename(tfilename,ffilename+".mp4")
    #sys.stdout.write(ERASE_LINE)
    print("Video downloaded")
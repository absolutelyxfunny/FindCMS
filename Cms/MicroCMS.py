from bs4 import BeautifulSoup
from colorama import Fore, init

class MicroCMS:

    def isMicroCMS(self, url):
        try:

            init()
        
            if "images.microcms-asset" in self.request.text:

                print(Fore.LIGHTGREEN_EX, f"[+] MicroCMS: {url}", flush = True)
        except:
            pass
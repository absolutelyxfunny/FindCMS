from bs4 import BeautifulSoup
from colorama import Fore, init

class DatoCMS:

    def isDatoCMS(self, url):
        try:
            init()
        

            if "datocms-assets.com" in self.request.text:

                print(Fore.LIGHTGREEN_EX,f"[+] DatoCMS: {url}", flush = True)
                return True
        except:
            pass
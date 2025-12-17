import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

class ModxCMS:

    def isModx(self,url):
        try:
            
            init()

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special MODX headers", flush = True)
            if "MODX Revolution" in self.request.headers:

                print(Fore.LIGHTGREEN_EX,f"[+] MODX: {url}", flush = True)
                return True
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding MODX Admin Panel", flush = True)

            modx_manager = requests.get(f"{url}/manager")
            if "modx-logo-color.svg" in modx_manager.text:
                print(Fore.LIGHTGREEN_EX,f"[+] MODX: {url}", flush = True)
                return True
        except:
            pass
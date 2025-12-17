import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

class CraftCMS:

    def __init__(self):
        pass

    def isCraftCMS(self, url):
        try:
            #init()
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding CraftCMS headers", flush = True)
            if "Craft Commerce" in self.request.headers or "Craft CMS" in self.request.headers:

                print(f"[+] CraftCMS: {url}", flush = True)
                return True

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding CraftCMS csrf token", flush = True)
            administrator = requests.get(f"{url}/admin/login")
            if administrator.status_code == 200 and "CRAFT_CSRF_TOKEN" in administrator.headers:
                print(f"[+] CraftCMS: {url}", flush = True)
        except:
            pass
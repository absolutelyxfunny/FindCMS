from bs4 import BeautifulSoup
from colorama import Fore, init

class PrestaShopCMS:

    def __init__(self):
        pass


    def isPrestaShop(self, url):
        try:

            init()

            prestashopcookies = self.request.cookies
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding PrestaShop cookies", flush = True)

            if "PrestaShop" in prestashopcookies:
                print(Fore.LIGHTGREEN_EX,f"[+] PrestaShop: {url}", flush = True)

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Checking PrestaShop htmltag", flush=True)
            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "PrestaShop" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] PrestaShop: {url}", flush=True)
                    return True
        except:
            pass
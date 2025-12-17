
from bs4 import BeautifulSoup
from colorama import Fore, init


class TildaCMS:

    def __init__(self):
        pass

    def isTilda(self, url):
        try:

            init()
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Tilda headers", flush = True)

            if "x-tilda-imprint" in self.request.headers or "x-tilda-server" in self.request.headers:
                print(Fore.LIGHTGREEN_EX, f"[+] Tilda: {url}", flush = True)
                return True
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Tilda scripts", flush= True)

            soup = BeautifulSoup(self.request.text, "lxml")
            scripts = soup.find_all("script")
        
            for script in scripts:
                if "tildacdn.com" in script:
                    print(Fore.LIGHTGREEN_EX, f"[+] Tilda: {url}", flush = True)
                    return True
        except:
            pass
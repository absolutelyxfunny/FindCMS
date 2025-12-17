from bs4 import BeautifulSoup
from colorama import Fore, init

class OctoberCMS:
    
    def isOctoberCMS(self,url):
        try:
            init()

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding OctoberCMS cookies", flush = True)
            
            if "october_session" in self.request.cookies:
                print(Fore.LIGHTGREEN_EX,f"[+] OctoberCMS: {url}", flush = True)
        except:
            pass
from bs4 import BeautifulSoup
from colorama import Fore, init

class WixCMS:

    def isWix(self, url):
        try:
            
            init()

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special Wix cookies", flush = True)

            if "x-wix-request-id" in self.request.headers:
                print(Fore.LIGHTGREEN_EX,f"[+] Wix: {url}", flush = True)
                return True
        
        
            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "Wix.com" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] Wix: {url}", flush = True)
                    return True
        
            if "static.wixstatic.com" in self.request.text:
                print(Fore.LIGHTGREEN_EX,f"[+] Wix: {url}", flush = True)
                return True
        except:
            pass
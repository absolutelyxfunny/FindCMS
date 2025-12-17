from bs4 import BeautifulSoup
from colorama import Fore, init

class Typo3CMS:

    def isTypo3(self, url):
        try:
            
            init()

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding TYPO3 cookies", flush = True)

            if "typo3-host" in self.request.cookies:
                print(Fore.LIGHTGREEN_EX,f"[+] TYPO3: {url}", flush = True)
                return True
        
            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "TYPO3 CMS" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] TYPO3: {url}", flush = True)
                    return True
        except:
            pass
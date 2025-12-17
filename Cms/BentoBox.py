from bs4 import BeautifulSoup
from colorama import Fore, init

class BentoBoxCMS:

    def isBento(self, url):
        try:

            init()
            self.BentoBoxWords = ["images.getbento.com", "theme-assets.getbento.com", "app-assets.getbento.com"]

            if "Powered by BentoBox http://getbento.com" in self.request.text:

                print(Fore.LIGHTGREEN_EX, f"[+] BentoBox: {url}", flush = True)
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Checking special BentoBox html tags", flush = True)
            if any(word in self.request.text for word in self.BentoBoxWords):
                print(Fore.LIGHTGREEN_EX, f"[+] BentoBox: {url}", flush = True)
        except:
            pass
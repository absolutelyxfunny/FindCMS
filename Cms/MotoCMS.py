from bs4 import BeautifulSoup
from colorama import Fore, init

class MotoCMS:

    def isMotoCMS(self, url):
        try:

            init()

            self.SpecialMotoWords = ["/mt-includes/js", "/mt-content/plugins"]

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special MotoCMS html tags", flush = True)

            if any(word in self.request.text for word in self.SpecialMotoWords):
                print(Fore.LIGHTGREEN_EX,f"[+] MotoCMS: {url}", flush = True)
                return True
        except:
            pass
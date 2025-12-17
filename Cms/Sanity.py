from bs4 import BeautifulSoup
from colorama import Fore, init

class SanityCMS:

    def isSanity(self, url):
        try:
            
            init()

            self.SanitySpecialWords = ["sanity.io", "sanity-images"]

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Sanity headers", flush = True)
            
            if "cdn.sanity.io" in self.request.headers:
                print(Fore.LIGHTGREEN_EX,f"[+] Sanity: {url}", flush = True)
                return True

            if any(word in self.request.text for word in self.SanitySpecialWords):
                print(Fore.LIGHTGREEN_EX, f"[+] Sanity: {url}", flush = True)
                return True
        except:
            pass
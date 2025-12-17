from bs4 import BeautifulSoup
from colorama import Fore, init

class PrismicCMS:

    def isPrismic(self, url):
        try:

            init()
            
            if "cdn.prismic.io" in self.request.text:

                print(Fore.LIGHTGREEN_EX, f"[+] [{url}] Prismic: {url}", flush=True)
                return True
        except:
            pass
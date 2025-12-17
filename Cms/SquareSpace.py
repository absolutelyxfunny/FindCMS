from bs4 import BeautifulSoup
from colorama import Fore, init

class SquareSpaceCMS:

    def isSquareSpace(self, url):
        try:
            
            init()

            if "squarespace-cdn.com" in self.request.text or "squarespace.com" in self.request.text:

                print(Fore.LIGHTGREEN_EX,f"[+] SquareSpace: {url}", flush = True)

        except:
            pass
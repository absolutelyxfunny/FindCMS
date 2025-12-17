from bs4 import BeautifulSoup
from colorama import Fore, init

class NeosCMS:

    def isNeos(self, url):
        try:

            init()
            
            if """This website is powered by Neos, the Open Source Content Application Platform licensed under the GNU/GPL.
    Neos is based on Flow, a powerful PHP application framework licensed under the MIT license.
    More information and contribution opportunities at https://www.neos.io""" in self.request.text:
                print(Fore.LIGHTGREEN_EX, f"[+] Neos: {url}", flush = True)
        except:
            pass

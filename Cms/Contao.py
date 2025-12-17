from bs4 import BeautifulSoup
from colorama import Fore, init

class ContaoCMS:

    def isContao(self,url):
        try:

            init()

            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "Contao Open Source CMS" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] Contao: {url}", flush = True)
                    return True
        except:
            pass
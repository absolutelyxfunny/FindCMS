from bs4 import BeautifulSoup
from colorama import Fore, init

class WeeblyCMS:

    def isWeebly(self, url):
        try:
            
            init()

            self.WeeblyMessages = ["weebly.com/weebly/apps", "weebly.com/uploads", "weebly-file"]
            try:
                soup = BeautifulSoup(self.request.text, "lxml")
                weeblyicon = soup.find("link", rel = "icon")

                if "weebly.com" in weeblyicon:
                    print(Fore.LIGHTGREEN_EX, f"[+] Weebly: {url}", flush = True)
                    return True
            except:
                pass
            if self.args.verbose == True:

                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special Weebly html tags")

            if any(word in self.request.text for word in self.WeeblyMessages):
                print(Fore.LIGHTGREEN_EX, f"[+] Weebly: {url}", flush = True)
                return True
        except:
            pass
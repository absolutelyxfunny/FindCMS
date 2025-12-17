from bs4 import BeautifulSoup
from colorama import Fore, init

class WordPressCMS:

    def isWordPress(self,url):

        init()

        try:

            self.WordPressWords = ["wp-content/plugins", "wp-content/themes"]

            if self.args.verbose == True:

                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special WordPress htmltags")
        
            if any(word in self.request.text for word in self.WordPressWords):
                    print(Fore.LIGHTGREEN_EX, f"[+] WordPress: {url}", flush = True)
                    return True

            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "WordPress" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] WordPress: {url}", flush = True)
                    return True
        except:
             pass
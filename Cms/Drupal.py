from bs4 import BeautifulSoup
from colorama import Fore, init

class DrupalCMS:

    def __init__(self):
        pass
    
    def isDrupal(self, url):

        try:

            init()
            
            self.DrupalMessages = ["data-drupal-messages", "data-drupal-link", "data-drupal-selector"]
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special Drupal headers", flush = True)
            if "Drupal-Cache" in self.request.headers or "Drupal-Dynamic" in self.request.headers:
                print(Fore.LIGHTGREEN_EX, f"[+] Drupal: {url}", flush = True)
                return True
        

            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})
        
            for version in get_meta:
                content = version.get("content", "")
                if "drupal.org" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] Drupal: {url}", flush = True)
                    return True
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special Drupal html tags", flush = True)
            if any(word in self.request.text for word in self.DrupalMessages):
                print(Fore.LIGHTGREEN_EX,f"[+] Drupal: {url}", flush = True)
                return True
        except:
            pass
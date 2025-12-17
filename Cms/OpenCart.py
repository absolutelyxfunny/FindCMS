import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

class OpenCartCMS:

    def __init__(self):
        
        pass
    
    def IsOpenCart(self, url):
        try:
        
            init()
            self.OpenCartMatchers = ["?route=product", "?route=information"]
            self.OpenCartMessages = ["OpenCart is open source software and you are free to remove the powered by OpenCart if you want, but its generally accepted practise to make a small donation.", 
                                 "<!-- Theme created by Shoputils & Katilina for OpenCart/ocStore 2.x"]


            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Checking OpenCart routes", flush = True)

            if any(word in self.request.text for word in self.OpenCartMatchers):
                print(Fore.LIGHTGREEN_EX, f"[+] OpenCart: {url}", flush = True)
                return True
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Checking special OpenCart messages", flush = True)
            for message in self.OpenCartMessages:
                if message in self.request.text:
                    print(Fore.LIGHTGREEN_EX, f"[+] OpenCart: {url}", flush = True)
                    return True
                

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding OpenCart admin panel")
            send = requests.get(f"{url}/admin", headers=self.Headers, cookies={"beget": "begetok"})
            if send.status_code == 200 and "http://www.opencart.com" in send.text: #добавить прочек на простой OpenCart
                print(Fore.LIGHTGREEN_EX, f"[+] OpenCart: {url}", flush = True) # над добавить сейв админок
                return True
            return False
        except:
            pass

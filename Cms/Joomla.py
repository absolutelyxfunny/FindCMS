import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

class JoomlaCMS:

    def __init__(self):
        pass
    
    def isJoomla(self, url):
        try:

            init()

            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Joomla htmltag", flush= True)

            soup = BeautifulSoup(self.request.text, "lxml")
            get_meta = soup.find_all("meta", attrs={"name": "generator"})

            for version in get_meta:
                content = version.get("content", "")
                if "Joomla" in content:
                    print(Fore.LIGHTGREEN_EX, f"[+] Joomla: {url}", flush = True)
                    return True
            
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Joomla special files", flush=True)

            language_files = requests.get(f"{url}/language/en-GB/en-GB.xml", headers=self.Headers)
            if language_files.status_code == 200:
                if "admin@joomla.org" in language_files.text:
                    print(Fore.LIGHTGREEN_EX, f"[+] Joomla: {url}", flush = True)
                    return True
        except:
            pass
     
    
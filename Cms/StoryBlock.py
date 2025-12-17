from bs4 import BeautifulSoup
from colorama import Fore, init

class StoryBlokCMS:

    def isStoryBlok(self, url):
        try:

            init()
            
            soup = BeautifulSoup(self.request.text, "lxml")
            images = soup.find_all("img")
        
            matches = 0

            for image in images:
                if "a.storyblok.com" in image:
                    matches+=1
                    if matches > 3:
                        print(Fore.LIGHTGREEN_EX, f"[+] StoryBlok: {url}", flush = True)
                        return True
        except:
            pass

from bs4 import BeautifulSoup
from colorama import Fore, init

class MagentoCMS:

    def isMagento(self,url):
        try:

            init()

            self.MagentoCookies = ["mage-banners-cache-storage", "mage-cache-storage", "mage-cache-storage-section-invalidation",
            "mage-cache-sessid", "mage-messages"]

            self.MagentoSpecialWords = ["Magento_Ui/js/lib", "Magento_Customer/js", "Magento_ReCaptchaFrontendUi/js",
            "Magento_Catalog/js/product", "Magento_Security/js", "Have no fear, help is near! There are many ways you can get back on track with Magento Store",
            ]
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding Magento cookies", flush = True)

            if any(word in self.request.cookies for word in self.MagentoCookies):
                print(Fore.LIGHTGREEN_EX,f"[+] Magento: {url}", flush = True)
                return True
        
            if self.args.verbose == True:
                print(Fore.LIGHTYELLOW_EX, f"[*] [{url}] Finding special Magento html tags", flush = True)

            if any(word in self.request.text for word in self.MagentoSpecialWords):
                print(Fore.LIGHTGREEN_EX,f"[+] Magento: {url}", flush = True)
                return True
        except:
            pass

from Cms import *
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

file_lock = Lock()

class ScanCMS:

    def __init__(self):
        pass

    def StartScan(self, url): # Большая часть конкретно этой функции была написана при помощи нейронки, поэтому возможен говнокод

        cms_checks = {
            "prestashop": lambda self, url: PrestaShopCMS.isPrestaShop(self, url),
            "opencart": lambda self, url: OpenCartCMS.IsOpenCart(self, url),
            "joomla": lambda self, url: JoomlaCMS.isJoomla(self, url),
            "craftcms": lambda self, url: CraftCMS.isCraftCMS(self, url),
            "tilda": lambda self, url: TildaCMS.isTilda(self, url),
            "octobercms": lambda self, url: OctoberCMS.isOctoberCMS(self, url),
            "wix": lambda self, url: WixCMS.isWix(self, url),
            "typo3": lambda self, url: Typo3CMS.isTypo3(self, url),
            "weebly": lambda self, url: WeeblyCMS.isWeebly(self, url),
            "magento": lambda self, url: MagentoCMS.isMagento(self, url),
            "prismic": lambda self, url: PrismicCMS.isPrismic(self, url),
            "sanity": lambda self, url: SanityCMS.isSanity(self, url),
            "modx": lambda self, url: ModxCMS.isModx(self, url),
            "storyblock": lambda self, url: StoryBlokCMS.isStoryBlok(self, url),
            "squarespace": lambda self, url: SquareSpaceCMS.isSquareSpace(self, url),
            "neos": lambda self, url: NeosCMS.isNeos(self, url),
            "datocms": lambda self, url: DatoCMS.isDatoCMS(self, url),
            "motocms": lambda self, url: MotoCMS.isMotoCMS(self, url),
            "drupal": lambda self, url: DrupalCMS.isDrupal(self, url),
            "contao": lambda self, url: ContaoCMS.isContao(self, url),
            "wordpress": lambda self, url: WordPressCMS.isWordPress(self, url),
            "bentobox": lambda self, url: BentoBoxCMS.isBento(self,url),
            "microcms": lambda self, url: MicroCMS.isMicroCMS(self,url)
        }

        if self.args.cms:
            cms = self.args.cms.lower()
            cms_checks[cms](self, url)
            cms_checks = {cms: cms_checks[cms]}  

        def RunScan(name, check_func):
            try:
                if check_func(self, url):
                    return name
            except:
                pass
            return None

        with ThreadPoolExecutor(max_workers=self.args.threads) as executor:
            if self.args.output:
                outfile = open(f"{self.args.output}", "a", encoding="utf-8")
            

            futures = {executor.submit(RunScan, name, func): name for name, func in cms_checks.items()}

            for future in as_completed(futures):
                result = future.result()
                if result:
                    if self.args.output:
                        with file_lock:
                            outfile.write(f"{url}|{result}\n")
        if self.args.output:
            outfile.close()

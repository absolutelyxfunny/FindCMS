import requests
import platform
import json
import argparse
import os
from bs4 import BeautifulSoup
from colorama import Fore, init
from Cms.OpenCart import OpenCartCMS
from Cms.PrestaShop import PrestaShopCMS
from CmsScanner.Scanner import ScanCMS
from CleanFile import FileCleaner
from concurrent.futures import ThreadPoolExecutor, as_completed


class CmsChecker:

    def __init__(self):
        
        if platform.system() == "Windows":

            os.system("cls")
        else:
            os.system("clear")
        
        print("""
 \t\t ______ _           _  _____ __  __  _____ 
 \t\t|  ____(_)         | |/ ____|  \/  |/ ____|
 \t\t| |__   _ _ __   __| | |    | \  / | (___  
 \t\t|  __| | | '_ \ / _` | |    | |\/| |\___ \ 
 \t\t| |    | | | | | (_| | |____| |  | |____) |
 \t\t|_|    |_|_| |_|\__,_|\_____|_|  |_|_____/ 
                                            
                                            """)
        
        
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-u", "--url", help = "Target URL to scan", required=False)
        self.parser.add_argument("-f", "--file", help = "File which contains urls or domains", required=False)
        self.parser.add_argument("-v", "--verbose", action="store_true", default=False, help = "Show verbose scanning", required=False)
        self.parser.add_argument("-o", "--output", help = "Output file to save targets", required=False)
        self.parser.add_argument("-c", "--cms", help = "Choose cms to check", required=False)
        self.parser.add_argument("-t", "--threads", help = "Number of threads to scan, default is 20", required=False)
        self.args = self.parser.parse_args()

        self.Headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Mobile Safari/537.36",
            "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",}


    def CheckArguments(self):

        if self.args.file == None and self.args.url == None:
            print(Fore.LIGHTYELLOW_EX,"[*] File and URL are empty, try findcms.py -h")
            init()
        
        if self.args.threads:
            self.args.threads = int(self.args.threads)
        else:
            self.args.threads = 20

        if self.args.file:

            links = FileCleaner.Cleaner(self)
            print(Fore.LIGHTGREEN_EX, f"[+] Targets loaded for scan: {len(links)}")
            self.LargeScan(links)


        if self.args.url:

            url = self.args.url.strip("/")
            if "http" not in url:
                url = f"http://{url}"

            print(Fore.LIGHTYELLOW_EX, f"[*] Target URL: {url}")
            print(Fore.LIGHTYELLOW_EX, f"[*] Checking connection to URL: {url}")
            try:
                self.request = requests.get(url, headers=self.Headers, verify=False, timeout=10)
                if self.request.status_code < 400:
                    ScanCMS.StartScan(self, url)
                    
                else:
                    print(Fore.RED, F"\n [-] There is problem with {url}")
            except Exception as e:
                print(Fore.RED, F"\n [-] There is problem with {url}")
            init()
    
    def SingleScan(self, url):
        self.request = requests.get(url, headers=self.Headers, timeout=5)
        ScanCMS.StartScan(self, url)
    
    def LargeScan(self,urls):
        with ThreadPoolExecutor(max_workers=30) as executor:
            executor.map(self.SingleScan, urls)

        
    

cms = CmsChecker()
cms.CheckArguments()





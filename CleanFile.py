from colorama import Fore, init

class FileCleaner:

    def Cleaner(self):
        print(Fore.LIGHTYELLOW_EX, "[*] Checking the file, please wait")

        seen = set()
        links = []

        with open(self.args.file, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().strip("/")

                if "http" not in line:
                    line = f"https://{line}"

                if line not in seen:
                    seen.add(line)
                    links.append(line)

        init()
        return links

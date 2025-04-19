import json
import requests
import re
import sys

def print_banner():
    print(r"""
            _ ____             _    _ _       _             
           | |  _ \           | |  | (_)     | |            
 _   _ _ __| | |_) | __ _  ___| | _| |_ _ __ | | _____ _ __ 
| | | | '__| |  _ < / _` |/ __| |/ / | | '_ \| |/ / _ \ '__|
| |_| | |  | | |_) | (_| | (__|   <| | | | | |   <  __/ |   
 \__,_|_|  |_|____/ \__,_|\___|_|\_\_|_|_| |_|_|\_\___|_|   

                                             H4-cklinker - wmdark.com
    """)

def main():
    try:
        print_banner()

        # Use your desired site automatically
        site = "multiculturaltoolbox.com"

        with open("urlbacklinks.json", "r") as file:
            data = json.load(file)

            for backlink in data:
                url = backlink['url'].replace("multiculturaltoolbox.com", site)

                try:
                    response = requests.get(url, timeout=5)  # Added timeout for safety
                    status = response.status_code
                except requests.RequestException as e:
                    status = "error"

                try:
                    domain = re.search(r'http://.*?/', url).group(0).replace("/", "").replace("http:", "")
                except AttributeError:
                    domain = "invalid-url"

                print(f"{site} => Backlink Eklendi ==> {domain} status: {status}")

    except Exception as e:
        print(f"\n\n => exit due to error: {e}\n")

if __name__ == "__main__":
    main()

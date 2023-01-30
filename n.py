import argparse
import re
import requests
import time
import plyer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", required=True, help="The URL of the website to check")
    parser.add_argument("--ignore", default=None, help="A regex pattern to ignore in the comparison")
    args = parser.parse_args()

    site = args.site
    ignore = args.ignore
    if ignore:
        ignore = re.compile(ignore)

    previous_content = ""
    while True:
        response = requests.get(site)
        current_content = response.text
        if ignore:
            current_content = re.sub(ignore, '', current_content)

        if previous_content and current_content != previous_content:
            plyer.notification.notify(
                title="Website Content Changed",
                message="The content of the website has changed!",
                app_name="Website Monitor",
                timeout=5
            )

        previous_content = current_content
        time.sleep(10)

if __name__ == "__main__":
    main()

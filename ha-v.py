import requests
import argparse

def get_latest_version():
    # Make a request to the Home Assistant API
    response = requests.get("https://api.github.com/repos/home-assistant/home-assistant/releases/latest")
    data = response.json()
    version = data["tag_name"]

    return version

def get_latest_hacs_version():
    # Make a request to the HACS API
    response = requests.get("https://api.github.com/repos/hacs/integration/releases/latest")
    data = response.json()
    version = data["tag_name"]

    return version


def main():
    home_assistant_version = get_latest_version()
    hacs_version = get_latest_hacs_version()

    # Print the versions
    print(f"--------------------------------------------------------------------")
    print(f"The latest version of \033[1mHome Assistant\033[0m is {home_assistant_version}.")
    print(f"The latest version of \033[1mHACS\033[0m is {hacs_version}.")
    print(f"--------------------------------------------------------------------")


if __name__ == "__main__":
    main()


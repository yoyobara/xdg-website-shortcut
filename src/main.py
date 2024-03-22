from argparse import ArgumentParser
from urllib.parse import urlparse

def parse_arguments():
    parser = ArgumentParser(prog="xdg shortcut creator",
                            description="create shortcuts to websites on xdg")

    parser.add_argument("u", "url", required=True, type=str, help="the url of the website")

    return parser.parse_args()

def get_icons():
    """
    fetches icon
    """


def main():
    args = parse_arguments()

    parsed_url = urlparse(args.url)

if __name__ == "__main__":
    main()

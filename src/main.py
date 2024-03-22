from argparse import ArgumentParser

def parse_arguments():
    parser = ArgumentParser(prog="xdg shortcut creator",
                            description="create shortcuts to websites on xdg")

    parser.add_argument("u", "url", required=True, type=str, help="")

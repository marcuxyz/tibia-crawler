from importlib import import_module
import argparse


def main():
    module = _import_module()
    parsed = get_flag()
    return module.Character(parsed.name)


def _import_module():
    return import_module("tibia")


def get_flag():
    parser = argparse.ArgumentParser(description="Calling crawler")
    subparser = parser.add_subparsers()
    crawler = subparser.add_parser("crawler")
    crawler.add_argument("--name", help="Nome do personagem do tibia")
    return parser.parse_args()


if __name__ == "__main__":
    main()

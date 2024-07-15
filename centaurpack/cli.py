import argparse
import sys
from .pack import pack_directory
from .unpack import unpack_file

VERSION = "0.1.0"


def main():
    parser = argparse.ArgumentParser(
        description="CentaurPack: Pack and unpack directory structures."
    )
    parser.add_argument("--version", action="version", version=f"CentaurPack {VERSION}")
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Increase output verbosity"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Pack command
    pack_parser = subparsers.add_parser(
        "pack", help="Pack a directory into a single file"
    )
    pack_parser.add_argument("directory", help="Directory to pack")
    pack_parser.add_argument("output", help="Output file name")

    # Unpack command
    unpack_parser = subparsers.add_parser("unpack", help="Unpack a centaurpack file")
    unpack_parser.add_argument("file", help="CentaurPack file to unpack")
    unpack_parser.add_argument("output", help="Output directory")

    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode enabled")

    if args.command == "pack":
        pack_directory(args.directory, args.output, verbose=args.verbose)
    elif args.command == "unpack":
        unpack_file(args.file, args.output, verbose=args.verbose)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

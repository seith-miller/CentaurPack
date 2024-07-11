import argparse
from pack import pack_directory
from unpack import unpack_file

def main():
    parser = argparse.ArgumentParser(description='Flatpack: Pack and unpack directory structures.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    pack_parser = subparsers.add_parser('pack', help='Pack a directory into a single file')
    pack_parser.add_argument('directory', help='Directory to pack')
    pack_parser.add_argument('output', help='Output file name')

    unpack_parser = subparsers.add_parser('unpack', help='Unpack a flatpack file')
    unpack_parser.add_argument('file', help='Flatpack file to unpack')
    unpack_parser.add_argument('output', help='Output directory')

    args = parser.parse_args()

    if args.command == 'pack':
        pack_directory(args.directory, args.output)
    elif args.command == 'unpack':
        unpack_file(args.file, args.output)

if __name__ == '__main__':
    main()
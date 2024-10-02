import hashlib as hb
import argparse
from argon2 import PasswordHasher
import pyfiglet
import os
import sys


def calculate_hash(filepath, hash_method):
    file_size = os.path.getsize(filepath)
    bytes_hashed = 0

    if hash_method == "argon2":
        return hash_argon2(filepath)

    hash_function = get_hash_function(hash_method)

    with open(filepath, "rb") as file:
        while chunk := file.read(4096):
            hash_function.update(chunk)
            bytes_hashed += len(chunk)
            progress = (bytes_hashed / file_size) * 100
            show_progress(progress)

    print("\nHashing complete!")  
    return get_final_hash(hash_function, hash_method)


def show_progress(progress):
    bar_length = 50
    block = int(bar_length * progress / 100)
    text = f"\rProgress: [{'#' * block + '-' * (bar_length - block)}] {progress:.2f}%"
    sys.stdout.write(text)
    sys.stdout.flush()


def get_hash_function(hash_method):
    hash_methods = {
        "sha3_256": hb.sha3_256,
        "blake2b": hb.blake2b,
        "md5": hb.md5,
        "sha1": hb.sha1,
        "sha224": hb.sha224,
        "sha256": hb.sha256,
        "sha384": hb.sha384,
        "sha512": hb.sha512,
        "ripemd160": lambda: hb.new("ripemd160"),
        "sha512_256": hb.sha512, 
    }

    if hash_method in hash_methods:
        return hash_methods[hash_method]()
    else:
        raise ValueError("Unsupported hash method!")


def hash_argon2(filepath):
    with open(filepath, "rb") as file:
        content = file.read()
    hasher = PasswordHasher()
    return hasher.hash(content)


def get_final_hash(hash_function, hash_method):
    if hash_method == "sha512_256":
        return hash_function.digest()[:32].hex()
    return hash_function.hexdigest()


def display_title():
    title = pyfiglet.figlet_format("Hasher")
    border = '*' * 50
    print(border)
    print(title)
    print("GitHub: https://github.com/shamali1013/Hasher/")
    print(border + "\n")


def parse_arguments():
    
    parser = argparse.ArgumentParser(description="Hash a file using specified method.")
    parser.add_argument('-m', '--method', required=True,
                        choices=['sha3_256', 'blake2b', 'md5', 'sha1', 'sha224',
                                 'sha256', 'sha384', 'sha512', 'sha512_256',
                                 'ripemd160', 'argon2'],
                        help="Hashing method:")
    parser.add_argument('-f', '--filepath', required=True, help="Path to the file to hash")
    parser.add_argument('-o', '--output', help="Output file to save the hash")
    return parser.parse_args()


def main():
    
    display_title()
    args = parse_arguments()

    try:
        hash_value = calculate_hash(args.filepath, args.method)
        print(f"{args.method.upper()} Hash of the file '{args.filepath}': \n{hash_value}")

        if args.output:
            with open(args.output, 'w') as out_file:
                out_file.write(f"{args.method.upper()} Hash: {hash_value}\n")
            print(f"\nHash saved to '{args.output}'")
    except FileNotFoundError:
        print(f"Error: File '{args.filepath}' not found.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

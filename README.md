# Hasher

Hasher is a simple command-line tool for calculating the hash of files using various hashing algorithms. It supports multiple hash methods, including SHA3-256, BLAKE2b, MD5, and Argon2.

## Features

- Calculate hashes using popular algorithms:
  - SHA3-256
  - BLAKE2b
  - MD5
  - SHA1
  - SHA224
  - SHA256
  - SHA384
  - SHA512
  - SHA512/256
  - RIPEMD160
  - Argon2

- Option to save the calculated hash to an output file.

## Requirements

- Python 3.x
- `argon2-cffi` for Argon2 hashing
- `pyfiglet` for ASCII art display

## Installation

### Option 1: Clone the Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/shamali1013/Hasher.git
   cd Hasher
   ```

2. Create and activate a virtual environment (mandatory on Linux):
   ```bash
   # Create a virtual environment named 'venv'
   python -m venv venv
   
   # Activate the virtual environment
   # On Linux and macOS:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. Install the package:
   ```bash
   pip install .
   ```

4. Verify the installation:
   ```bash
   hasher --help
   ```


## Usage

Run the Hasher script from the command line:
```bash
hasher -m <hash_method> -f <filepath> [-o <output_file>]
```

### Arguments:
- `-m`, `--method`: The hashing method to use (required).
- `-f`, `--filepath`: Path to the file you want to hash (required).
- `-o`, `--output`: (Optional) Specify an output file to save the hash.

### Example
To calculate the SHA256 hash of a file named `example.txt` and save the output to `hash.txt`:
```bash
python hasher.py -m sha256 -f example.txt -o hash.txt
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Feel free to contribute to this project by creating issues or submitting pull requests.

## Contact

For questions or feedback, please reach out:

- GitHub: [shamali1013](https://github.com/shamali1013)
- Email: [shamikhmushtaq1013@gmail.com](mailto:shamikhmushtaq1013@gmail.com)

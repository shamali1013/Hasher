from setuptools import setup, find_packages

setup(
    name='hasher',
    version='1.0.0',
    author='Sham Ali',
    author_email='shamikhmushtaq1013@gmail.com',
    description='A tool to calculate file hashes using various algorithms',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shamali1013/Hasher/',
    packages=find_packages(),  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0,<4',
    install_requires=[
        'argon2-cffi',  # Required dependency
        'pyfiglet',     # Required dependency
    ],
    entry_points={
        'console_scripts': [
            'h4sher=Hasher.hasher:main',  
        ],
    },
)

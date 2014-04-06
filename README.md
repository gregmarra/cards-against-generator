cards-against-generator
=======================

Helps make Cards Against Humanity style playing cards.

Usage
-----
- Make input cards files in `/cards`, probably like `white.txt` and `black.txt`
- `mkdir cards` as the default output folder
- `python make_cards.py -c white -i cards/white.txt`
- `python make_cards.py -c black -i cards/black.txt`
- open `cards/`

`python make_cards.py -h` for help!

Customization
-------------
- You can specify a custom logo with `--footer-logo`
- You can specify custom footer text with `--footer-text`

Stuff I had to do to get PIL to work
------------------------------------
You have to install the PIL imaging library, but it is mostly abandoned, so you have to install Pillow instead.

### Installing Pillow
https://pypi.python.org/pypi/Pillow/2.2.1

### Fixing Issues
- http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa helped fix a `clang error: unknown argument: '-mno-fused-madd'` error.


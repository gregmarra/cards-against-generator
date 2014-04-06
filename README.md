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

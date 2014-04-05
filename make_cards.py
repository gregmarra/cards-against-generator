from optparse import OptionParser

from cardgenerator import CardGenerator

### Card Configuration
CONFIG = {
  "card_dimensions_px": (822, 1122),
  "card_padding_px": 64,
}

DEMO_CARDS = [
  "Raptor attacks.",
  "During high school, I never really fit in until I found _ club.",
]

def munge_text(text):
  return text.replace("_", "__________")

def main():
  parser = OptionParser()
  parser.add_option("-s", "--save_folder", type="string", default="cards",
                    help="folder to save output to")
  parser.add_option("-i", "--input_file", type="string", default="input.txt",
                    help="file to read from")
  parser.add_option("-c", "--color", type="string", default="white",
                    help="color scheme. white or black")
  
  options, args = parser.parse_args()

  config = CONFIG
  config["save_folder"] = options.save_folder
  config["color"] = options.color

  cg = CardGenerator(config)

  for card in DEMO_CARDS:
    text = munge_text(card)
    cg.writeCard(text)

  print("done.")

if __name__ == '__main__':
    main()

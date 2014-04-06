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
  parser.add_option("-c", "--color", type="string", default="white",
                    help="color scheme. white or black")
  parser.add_option("-f", "--footer_text", type="string", default="Cards Against Cards",
                    help="text for footer.")
  parser.add_option("-i", "--input_file", type="string", default="input.txt",
                    help="file to read from")
  parser.add_option("-l", "--footer_logo", type="string", default="source/logo.png",
                    help="logo for footer.")
  parser.add_option("-s", "--save_folder", type="string", default="cards",
                    help="folder to save output to")

  
  options, args = parser.parse_args()

  config = CONFIG
  config["color"] = options.color
  config["save_folder"] = options.save_folder
  config["footer_text"] = options.footer_text
  config["footer_logo"] = options.footer_logo
  
  cg = CardGenerator(config)

  for card in DEMO_CARDS:
    text = munge_text(card)
    cg.writeCard(text)

  cg.writeBack()

  print("done.")

if __name__ == '__main__':
    main()

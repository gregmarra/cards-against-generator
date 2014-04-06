import os
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

CHARS_PER_LINE = 20
FONT_PATH = "/Library/Fonts/Arial.ttf"
BODY_SIZE = 72
FOOTER_SIZE = 36

class CardGenerator(object):
  def __init__(self, config):
    self.save_folder = config["save_folder"]
    self.color = config["color"]
    self.card_dimensions = config["card_dimensions_px"]
    self.footer_text = config["footer_text"]
    self.index = 0
    self.padding = config["card_padding_px"]
    super(CardGenerator, self).__init__()

  @property
  def background_color(self):
    if self.color == "white":
      return (255, 255, 255, 255)
    else:
      return (0, 0, 0, 255)

  @property
  def foreground_color(self):
    if self.color == "white":
      return (0, 0, 0, 255)
    else:
      return (255, 255, 255, 255)

  def makeCard(self, text):
    card = Image.new("RGBA", (self.card_dimensions[0], self.card_dimensions[1]), self.background_color)
    draw = ImageDraw.Draw(card)

    # draw words
    body_font = ImageFont.truetype(FONT_PATH, BODY_SIZE)
    offset = self.padding
    for line in textwrap.wrap(text, width=CHARS_PER_LINE):
        draw.text((self.padding, offset), line, font=body_font, fill=self.foreground_color)
        offset += body_font.getsize(line)[1]

    # draw footer
    footer_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", FOOTER_SIZE)
    footer_offset = self.card_dimensions[1] - self.padding - footer_font.getsize(line)[1]
    draw.text((self.padding, footer_offset), self.footer_text, font=footer_font, fill=self.foreground_color)
    
    return card

  def writeCard(self, words):
    filename = u"{}.{}.png".format(self.index, self.color)
    self.index += 1
    card = self.makeCard(words)
    card.save(os.path.join(self.save_folder, filename))

  def makeBack(self):
    card = Image.new("RGBA", (self.card_dimensions[0], self.card_dimensions[1]), self.background_color)
    draw = ImageDraw.Draw(card)

    # draw words
    body_font = ImageFont.truetype(FONT_PATH, BODY_SIZE * 2)
    offset = self.padding
    for line in self.footer_text.split(" "):
        draw.text((self.padding, offset), line, font=body_font, fill=self.foreground_color)
        offset += body_font.getsize(line)[1] + 24

    return card

  def writeBack(self):
    card = self.makeBack()
    card.save(os.path.join(self.save_folder, "back.{}.png".format(self.color)))

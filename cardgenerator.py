import os
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

class CardGenerator(object):
  def __init__(self, config):
    self.save_folder = config["save_folder"]
    self.color = config["color"]
    self.card_dimensions = config["card_dimensions_px"]
    self.index = 0
    self.padding = config["card_padding_px"]
    super(CardGenerator, self).__init__()

  @property
  def background_color(self):
    if self.color == "white":
      return (255, 255, 255, 255)
    else:
      return (0, 0, 0, 0)

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
    body_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 72)
    offset = self.padding
    for line in textwrap.wrap(text, width=20):
        draw.text((self.padding, offset), line, font=body_font, fill=self.foreground_color)
        offset += body_font.getsize(line)[1]

    # draw footer
    footer_font = ImageFont.truetype("/Library/Fonts/Arial.ttf", 36)
    bottom_offset = self.card_dimensions[1] - self.padding - footer_font.getsize(line)[1]
    draw.text((self.padding, bottom_offset), "Cards against Olin", font=footer_font, fill=self.foreground_color)
    
    return card

  def writeCard(self, words):
    filename = u"{}.png".format(self.index)
    self.index += 1
    card = self.makeCard(words)
    card.save(os.path.join(self.save_folder, filename))

  def writeBlank(self):
    card = Image.new("RGBA", (CARD_WIDTH_PX, CARD_HEIGHT_PX), (255,255,255,255))
    card.save(os.path.join(self.save_folder, "blank.card.png"))
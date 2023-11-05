"""Build MemeEngine.

Ingest and parse.
"""
import uuid
from PIL import Image, ImageDraw, ImageFont


class MemeEngine:
    """Build MemeEngine.

    Init and make_meme.
    """

    def __init__(self, output_dir):
        """Return a boolean file is can ingest."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Return a boolean file is can ingest."""
        image = Image.open(img_path)
        if image.size[0] != width:
            width_percent = (width / float(image.size[0]))
            height = int((float(image.size[1]) * float(width_percent)))
            image.thumbnail((width, height), Image.LANCZOS)

        im_draw = ImageDraw.Draw(image)
        im_font = ImageFont.truetype('MemeGenerator/font/AlexBrush-Regular.ttf', 40)

        im_draw.text((10, 150), f'{text} - {author}', fill=(255, 0, 0), font=im_font)

        save_path = f"{self.output_dir}/meme-img-{str(uuid.uuid4())}.png"
        image.save(save_path)

        return save_path

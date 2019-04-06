#==============
# Author: Nuowen Kan, (https://main.nuowen.pro)
##=============

from PIL import Image, ImageDraw, ImageFont

BOX = [200, 200, 250, 250] # set the select region in the picture (left, upper, right, lower)
RESIZE_BOX = [400, 400] # set the width and height of resized region
PICTURE_INPUT_PATH = './test_map.jpg'
PICTURE_OUTPUT_PATH = './processed.jpg'

class PinP:
    def __init__(self, box=BOX, resize_box=RESIZE_BOX):
        self.box = box
        self.resize_box = resize_box

    def processing(self, input_path = PICTURE_INPUT_PATH, save_path = PICTURE_OUTPUT_PATH):
        im = Image.open(input_path) ## input the picture

        return_size = im.size # (width, height)

        region = im.crop(self.box) ## crop the region

        region = region.resize((self.resize_box[0], self.resize_box[1]),Image.LANCZOS) # (width, height) is the requested size in pixels, Image.LANCZOS is resampling filter(optional, refer to https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer)

        im.paste(region, box = (return_size[0] - self.resize_box[0], return_size[1] - self.resize_box[1]))

        outline = ImageDraw.Draw(im)
        outline.rectangle(self.box, outline = (255,0,0)) # draw the outline of selected region into red
        outline.rectangle([return_size[0] - self.resize_box[0], return_size[1] - self.resize_box[1], return_size[0], return_size[1]], outline = (255,0,0)) # draw the outline of selected region into red

        # im.show()

        im.save(save_path)




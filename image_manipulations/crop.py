from PIL import Image
from utils import *

def crop(state, block):
    img_width = state['image'].width
    img_height = state['image'].height
    width = block.slider(value=img_width, max_value=img_width, min_value=0, label='width')
    height = block.slider(value=img_height, max_value=img_height, min_value=0, label='height')
    state['image'].crop(((img_width - width) // 2,
                         (img_height - height) // 2,
                         (img_width + width) // 2,
                         (img_height + height) // 2))


from utils import *

def rgb_channels(state,block):
    img = state['image']
    default = 126
    r = block.slider('Red',value = default, min_value = 0,max_value = 255)
    g = block.slider('Green', value=default, min_value=0, max_value=255)
    b = block.slider('Blue', value= default, min_value=0, max_value=255)
    try:
        img[:, :, 0] += r - default
    except UFuncTypeError:

    img[:, :, 1] += g - default
    img[:, :, 2] += b - default
    state['image'] = img
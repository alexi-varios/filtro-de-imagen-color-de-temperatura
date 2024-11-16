from PIL import Image
import numpy as np

def color_temperature_filter_rgb(img, temperature):

    img = np.array(img)

    if temperature > 6500:
        factor_azul = (temperature - 6500) / 10000
        factor_rojo = 0.0 
    elif temperature > 6500:
        factor_rojo = (6500 - temperature) / 10000
        factor_azul = 0.0
    else:
        factor_rojo = 0.0
        factor_azul = 0.0

    img[:, :, 0] = img[:, :, 0] + (img[:, :, 0] * factor_rojo)
    img[:, :, 2] = img[:, :, 2] + (img[:, :, 2]* factor_azul)

    img = np.clip(img, 0, 255)

    return Image.fromarray(img.astype('uint8'))
#---------------------------------
# Author: Omar S. Gómez
# Date: March 2024
# Description: Example of a pipes and filter software architecture style responsible for apply different
#              image transformations through different filters, such as: brightness, contrast, saturation,
#              negative, flip and watermark text. 
#---------------------------------

from PIL import Image
from datetime import datetime
import requests
import io

#Filters
from filters.brightness_filter import brightness
from filters.contrast_filter import contrast
from filters.saturation_filter import saturation
from filters.negative_filter import negative
from filters.flip_filter import flip
from filters.watermark_filter import watermark
from filters.color_temperature import color_temperature_filter_rgb

#Load a random image
urlimg = "https://picsum.photos/200/300"
response = requests.get(urlimg)
image_data = io.BytesIO(response.content)
img = Image.open(image_data)

#Get current datetime
dt = datetime.now()

#Example of a pipes and filters architectural style
#img = brightness(img, 1.5)
 #img = negative(img)
#img = saturation(img, 1)
 #img = flip(img)
#img = contrast(img, 1.5)
#img = watermark(img, dt.strftime('%A'), 22)
img = color_temperature_filter_rgb(img, 3000)

#Output
img.show()


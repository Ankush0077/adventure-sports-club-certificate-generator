# import required classes
 
from PIL import Image, ImageDraw, ImageFont
 
# create Image object with the input image
 
image = Image.open('background.jpg')
 
# initialise the drawing context with
# the image object as background
 
draw = ImageDraw.Draw(image)
 
# create font object with the font file and specify
# desired size
 
font = ImageFont.truetype("Roboto-Light.ttf", 30)
 
# starting position of the message
 
(x, y) = (221, 680)
distance = "100 KM"
color = 'rgb(23, 63, 63)' # black color
 
# draw the message on the background
 
draw.text((x, y), distance, fill=color, font=font)

(x, y) = (810, 680)
time = '12 Hours'
color = 'rgb(23, 63, 63)' # white color
draw.text((x, y), time, fill=color, font=font)

font = ImageFont.truetype("Roboto-Light.ttf", 60)

(x,y) = (460,510)
name = 'Chidanand Jadar'
color = 'rgb(23, 63, 63)'
draw.text((x, y), name, fill=color, font=font)
 
# save the edited image
 
image.save('greeting_card.png')
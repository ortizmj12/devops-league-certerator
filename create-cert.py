#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

def x_coordinate(center_of_line, word):
    word_size = font.getsize(word)
    coordinate = center_of_line - (word_size[0]/2)
    return coordinate

date = datetime.today()
image = Image.open('devops-league-cert.png')
name_line_center = 400
month_line_center = 367
day_line_center = 507
year_line_center = 605
draw = ImageDraw.Draw(image)
color = 'rgb(64, 64, 66)'

font = ImageFont.truetype('RobotoMono-Bold.ttf', size=45)
name = input("Name: ")
(x, y) = (x_coordinate(name_line_center, name), 180)
draw.text((x, y), name, fill=color, font=font)

font = ImageFont.truetype('RobotoMono-Bold.ttf', size=35)
month = date.strftime('%B')
(x, y) = (x_coordinate(month_line_center, month), 308)
draw.text((x, y), month, fill=color, font=font)

day = date.strftime('%d')
(x, y) = (x_coordinate(day_line_center, day), 308)
draw.text((x, y), day, fill=color, font=font)

year = date.strftime('%Y')
(x, y) = (x_coordinate(year_line_center, year), 308)
draw.text((x, y), year, fill=color, font=font)

image.save('congratulations.png')

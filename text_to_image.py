#!/usr/bin/python3 

from PIL import Image, ImageDraw, ImageFont
import textwrap
import sys

width = 1920
height = 1080

if len(sys.argv) < 2 or sys.argv[1].strip() == "": 
    print("Please provide some text")
    exit()
quote_ja = sys.argv[1]
quote_en = sys.argv[2]
quote_ja.encode("utf-8")
quote_en.encode("utf-8")
img = Image.new('RGB', (width, height), color='black')

font_ubuntu = ImageFont.truetype('ubuntu.ttf', size=28)
font = ImageFont.truetype('CODE2000.TTF', size=32)

wrappedTextJa = textwrap.wrap(quote_ja, width=100)
wrappedTextEn = textwrap.wrap(quote_en, width=100)
quoteWrappedJa = ''
countLinesJa = 0
quoteWrappedEn = ''
for part in wrappedTextJa[:-1]:
    countLinesJa += 1
    quoteWrappedJa = quoteWrappedJa + part + '\n'
quoteWrappedJa += wrappedTextJa[-1]

for part in wrappedTextEn[:-1]:
    quoteWrappedEn = quoteWrappedEn + part + '\n'
quoteWrappedEn += wrappedTextEn[-1]

imgDraw = ImageDraw.Draw(img)
textWidth, textHeight = imgDraw.textsize(quoteWrappedJa, font=font)
xText = (width - textWidth) / 2
yText = (height - textHeight) / 2

imgDraw.text((xText, yText), quoteWrappedJa, font=font, fill=(255, 255, 255))

textWidthEn, textHeightEn = imgDraw.textsize(quoteWrappedEn, font=font_ubuntu)
xTextEn = (width - textWidthEn) / 2 
yTextEn = (height - textHeightEn) / 2
yTextEn += (textHeight * (countLinesJa + 1)) + 5

imgDraw.text((xTextEn, yTextEn), quoteWrappedEn, font=font_ubuntu, fill=(255, 255, 255))

img.save('result.png')

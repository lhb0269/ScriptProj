from PIL import ImageColor
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter

ImageColor.colormap.keys()

ImageColor.getcolor('red','RGBA')
ImageColor.getcolor('black','RGBA')
ImageColor.getcolor('red','CMYK')
ImageColor.getcolor('yellow','CMYK')

img = Image.open('x.jpg')

img2 = Image.open('cat.jpg')
bright = ImageEnhance.Brightness(img2)
bright_img2 = bright.enhance(1.5)

colored_cat_img = ImageEnhance.Color(img2).enhance(5.5)

contrasted_cat_image = ImageEnhance.Contrast(img2).enhance(1.5)

sharpened_cat_image = ImageEnhance.Sharpness(img2).enhance(3.0)

blurred_cat_image = img2.filter(ImageFilter.FIND_EDGES)

img = Image.new('RGBA',(100,200),'pink')

face_img = img2.crop((110,30,305,250))
img2.paste(face_img,(0,0))

width,height = img2.size
img2_small = img2.resize((width//2,height//2))

new_img = img2.rotate(45,expand = True)

new_img = img2.transpose(Image.FLIP_TOP_BOTTOM)

from PIL import ImageFont
im = Image.new('RGBA',(300,300),'white')
from PIL import ImageDraw
draw = ImageDraw.Draw(im)
draw.text((20,150),'지야스',fill='purple')
##PIL
from PIL import Image
import random

img = Image.open("C:/projects/python/testing/images/bert.jpg")
print(img.format, img.size, img.mode)
#img.show()
#img.close()

#rotate
#new_img = img.transpose(Image.ROTATE_180)
#new_img.show()
#new_img.close()

#crop
width, height = img.size
print(f"width: {width}, height: {height}")
left = width/3
top = height/3
right = 3*width/5
buttom = 3*height/5

print(f"left: {left}, top: {top}, right: {right}, buttom: {buttom}")
#imgCrop = img.crop((left,top,right,buttom))
#imgCrop.show()

#imgCrop.close()
#img.close()

def r():
      return random.randint(0,255)

im = Image.new('RGB', (1000, 1000))

list1 = [(r(),r(),r()) for i in range(0,1000000)]
#list1.sort()

im.putdata(list1)
im.show()
import math
from PIL import Image
from PIL import ImageDraw
import math

size = 400
coeff = float(input())
n = int(input())
# im = Image.new('RGB', (size, size), (255, 255, 255))

alpha = math.radians(int(45 / coeff))
factor = 1 / (math.sin(alpha) + math.cos(alpha))
size = 200
im = Image.new('RGB', (size, size), (255, 255, 255))
draw = ImageDraw.Draw(im)

for i in range(n):
    size = round(size)
    draw.rectangle((-size / 2, -size / 2, size, size), fill=(255, 255, 255), outline=(0, 0, 0))
    size = size * factor
    im.rotate(alpha)
im.save("im.png")
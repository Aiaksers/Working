from PIL import Image
from PIL import ImageDraw

width = 1000
height = 1000

image = Image.new("RGB", (width, height))

draw = ImageDraw.Draw(image)
draw.line((500, 500, 200, 600))
draw.line((200, 600, 250, 500))
draw.line((250, 500, 200, 400))
draw.line((200, 400, 500, 500))
draw.line((500, 500, 400, 200))
draw.line((400, 200, 500, 250))
draw.line((500, 250, 600, 200))
draw.line((600, 200, 500, 500))
draw.line((500, 500, 800, 600))
draw.line((800, 600, 750, 500))
draw.line((750, 500, 800, 400))
draw.line((800, 400, 500, 500))
draw.line((500, 500, 600, 800))
draw.line((600, 800, 500, 750))
draw.line((500,750, 400, 800))
draw.line((400, 800, 500, 500))
image.save("Тамплиеры.png", "PNG")
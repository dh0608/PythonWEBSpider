import pytesseract
import tesserocr
from PIL import Image

# 1.
image = Image.open('./images/tesseracttest.jpg')
text = pytesseract.image_to_string(image)
print(text)

# 2.
image = Image.open('./images/Code.jpg')
# 图片转化为灰度图
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)


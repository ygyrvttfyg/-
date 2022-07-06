'''
项目:代码实例
文件名:str_image
制作人:"黄涛"
date:2022/2/3
'''
from PIL import Image
img_name='20220203151017.jpg'
img = Image.open(img_name)
out=img.convert('L')
width,height=out.size
out=out.resize((int(width),int(height*0.5)))
width,height=out.size
asciis = "$@B%8&WM#*oawmZO0QUYXzcyunxrjf' "
img_text = ""
for row in range(height):
    for col in range(width):
        gray = out.getpixel((col,row))
        img_text += asciis[int(gray/225*26)]
    img_text += '\n'
with open(f'C:/Users/666666/Downloads/{img_name}.txt','w') as f:
    f.write(img_text)

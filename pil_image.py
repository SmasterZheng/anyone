from PIL import Image

img=Image.open("test.jpg")
img_size=img.size()[0]
img_palette=img.palette()
print("尺寸大小：",img_size)
print("像素高:",img_palette)
import base64
with open("test.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print(str)
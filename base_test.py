import base64


encodestr = base64.b64encode('abcr34r344r'.encode('utf-8'))

print(encodestr)
print(str(encodestr,'utf-8'))
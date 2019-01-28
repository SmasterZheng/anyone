import os

path_name="videos"
isExists=os.path.exists(path_name)
print(isExists)
if not isExists:
	os.makedirs(path_name)
	print(path_name,"创建成功！")
	# return True
else:
	print(path_name,"已存在")
	# return False
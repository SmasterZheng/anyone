# anyone
个人学习的任何代码（坚持每天都传一点）
从2019年开始  每天上github写一点点小东西  或者个人的项目



Git global setup
git config --global user.name "zhengxiaozhang WX591713"
git config --global user.email "zhengxiaozhang@huawei.com"

Create a new repository
git clone https://github.com/SmasterZheng/anyone.git
cd tf-serving-test
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master

Existing folder
cd existing_folder
git init
git remote add origin https://github.com/SmasterZheng/anyone.git
git add .
git commit
git push -u origin master

Existing Git repository
cd existing_repo
git remote add origin https://github.com/SmasterZheng/anyone.git
git push -u origin --all
git push -u origin --tags

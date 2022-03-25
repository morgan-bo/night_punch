# 免责声明
本项目仅仅用于学习交流用途，并非对国家政策的不支持，请各位同学坚持晚点名打卡！

# night_punch
电子科技大学晚打卡研究生版
# 使用方法
- 需要一台可以访问互联网的linux服务器
- 安装screen软件，以ubuntu为例，安装命令为：
```
apt update && apt install screen
```
- 安装python3.6或以上版本。
- 安装python的schedule库，用于定时执行脚本，命令为（安装到默认python3）：
```
pip3 install schedule
```
# 使用流程
### 配置payload信息
- 修改`night_punch/payload/`下的`night_xx.json`文件，将文名中的`xx`修改为自己想要的名字，并且可以复制多份分别命名，如：`night_aaa.json`、`night_bbb.json`、`night_ccc.json`
- 将`night_aaa.json`、`night_bbb.json`、`night_ccc.json`中的如下字段修改为对应打卡人的姓名和学号。
```
"field_1": "小张",
"field_2": "202xxxxxxxxx",
```
- 修改`night_punch/night_punch.py`中75行处的`nane_list`为上面步骤文件名中的`aaa`、`bbb`、`ccc`
```
name_list = ['aaa', 'bbb', 'ccc']
```
### 运行脚本
- 首先创建一个名字为**night_punch**的screen，用于在后台持续运行脚本：
```
screen -S night_punch
```
- 运行上面一行命令后会进入到一个新的页面，此时进入到**night_punch**的项目文件夹，并运行脚本：
```
python3 night_punch.py
```
- 运行上面一行命令后会进入阻塞状态，可以使用`ctrl`+`d`退出screen，screen可能用到的操作如下：
```
screen -S xxx: 创建名为xxx的screen并且进入其中；
ctrl + a + d: 退出当前screen且不杀掉该screen进程；
ctrl + d: 退出并杀掉当前screen进程；
screen -ls: 查看当前用户的所有screen；
screen -r xxx: 进入xxx的screen；
screen -D -r xxx: 在xxx有人进入的情况下，强行进入xxx
```
# 运行结果检查
- 进入到`night_punch/log/`文件夹，查看`daily.log`文件，里面记载了历史打卡信息，包括成功或失败的记录，如下例所示：
```
2022/03/20 19:11:38.238502, user=tb, code=200, succeed!
2022/03/21 19:12:04.377770, user=tb, code=200, succeed!
2022/03/22 19:13:18.387938, user=tb, code=200, succeed!
2022/03/23 19:13:47.583776, user=tb, code=200, succeed!
2022/03/24 19:09:16.716099, user=tb, code=200, succeed!
```

# EasyTrans

### 目的
* 看英文论文去各个翻译网站对比翻译结果的时间消耗。
* 下载翻译后的pdf以及word要花钱，如翻译狗，有道等。
### 实现
* 基于django、PyMuPdf、谷歌、有道翻译实现了pdf英译汉的功能，翻译后的pdf格式基本保持不变，可以下载docx和pdf格式的翻译文档，简单的满足看论文以及写总结的需求。
### 问题
* word不能实现pdf一样的排版，翻译后的pdf还是存在样式问题（需要考虑的很多，慢慢做优化）。
* 使用PyMuPdf写入图片，表格无法写入。
* 搜狗，百度翻译接口未实现。
* 有道翻译长句子有问题，建议谷歌。
### 环境 
> 开发环境的系统平台为 Windows 10 （64 位），Python 版本为 3.6 （64 位），Django版本为 2.2
 ```
atomicwrites==1.3.0
attrs==19.1.0
certifi==2019.3.9
chardet==3.0.4
colorama==0.4.1
Django==2.2.1
docx==0.2.4
idna==2.8
Js2Py==0.63
lxml==4.3.3
more-itertools==7.0.0
pdfminer3k==1.3.1
Pillow==6.0.0
pluggy==0.11.0
ply==3.11
py==1.8.0
PyExecJS==1.5.1
pyjsparser==2.7.1
PyMuPDF==1.14.13
PyPDF2==1.26.0
pytest==4.5.0
python-docx==0.8.10
pytz==2019.1
requests==2.21.0
six==1.12.0
sqlparse==0.3.0
tzlocal==1.5.1
urllib3==1.24.3
wcwidth==0.1.7
```
### 展示
![yasnhi1.gif](https://i.loli.net/2019/05/23/5ce6b013692cb50906.gif)
![yasnhi2.gif](https://i.loli.net/2019/05/23/5ce6b2e134b8a26386.gif)
![yasnhi.gif](https://i.loli.net/2019/05/23/5ce6af09b4dd645364.gif)
### 参考文档
[PyMuPDF参考文档](https://pymupdf.readthedocs.io/en/latest/)
### 在本地运行项目
#### 1.克隆项目到本地(不使用git工具的话，直接下载就ok)
打开命令行，进入到保存项目的文件夹，输入如下命令：<br>
`https://github.com/QPromise/Easy-Trans.git`
<br>
#### 2.创建并激活虚拟环境（不使用可以跳过这里）
强烈推荐在 Virtualenv 下进行 Django 的开发。Virtualenv 是一个 Python 工具，使用它可以创建一个独立的 Python 环境。<br>

在命令行进入到保存虚拟环境的文件夹()，输入如下命令创建并激活虚拟环境：
`C:\WINDOWS\system32>pip install virtualenv`<br>
`C:\WINDOWS\system32>virtualenv C:\Users\Envs\EasyTrans_env`
<br>
`C:\WINDOWS\system32>C:\Users\Envs\EasyTrans_env\Scripts\activate`
<br>
`(EasyTrans_env) C:\WINDOWS\system32>`
#### 3.安装项目依赖
![%(POS)~0M$(N5HXNAR$BUM.png](https://i.loli.net/2019/05/24/5ce76124bd5e058450.png)

如果使用了虚拟环境，确保激活并进入了虚拟环境，在命令行进入项目所在的 Easy-Trans 文件夹，运行如下命令：<br>
`pip install -r requirements.txt`
#### 4.数据库迁移
命令行输入<br>
`python manage.py makemigrations`<br>
`python manage.py migrate`
#### 5.创建后台管理员用户
命令行输入<br>
`python manage.py createsuperuser`
#### 6.运行开发服务器
命令行输入<br>
`python manage.py runserver`<br>
在浏览器输入：127.0.0.1:8000 就可以看到主页了。


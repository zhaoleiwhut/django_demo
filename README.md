# django_demo (Python 3.x)
这个项目仅供新人学习入门

## 安装和创建
1. 安装 python 
1. 安装 Django：pip install django
1. 创建项目：django-admin startproject django-demo1
1. 运行项目 cd django-demo1, 然后运行： python manage.py runserver 0.0.0.0:8888
1. 这个时候可以访问 http://localhost：8888
1. 此时停止进程，创建app1： python manage.py startapp app1
1. 创建 template、static 文件夹，分别用于放置模板和静态资源
1. 创建 views.py 

## Django 模型
创建好模型后，生成表结构：
```
python manage.py migrate # 创建全部表结构
python manage.py migrate app1 # 创建app1的表结构
python manage.py makemigrations app1 # 如果app中模型发生了变化需要同步
```

## 创建超级管理员
```
python manage.py createsuperuser
```
用户名输入admin，并输入密码 love******
打开 http://localhost:8888/admin/
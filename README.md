# 在线字典
## 1. 需求分析 --> 客户端该怎么用
    服务端 :  处理请求 处理数据

    客户端 :  发送请求 得到结果
    
## 2. 确定并发方案,确定套接字使用,确定细节
    并发:　多进程/多线程　
    套接字: tcp套接字
    细节 : 使用数据库处理数据,注册成功进入二级界面
           历史记录只看前10条, 注册信息 用户名 密码
## 3. 技术点
* 数据存储 dict 其他的数据表?
       单词表 : words (查单词)
       用户表 : user  (注册,登录)
       id  name  passwd

       create table user (id int primary key auto_increment,name varchar(20) not null,passwd char(64) not null);

       历史记录: hist  (查历史记录)
       uid  wid  time

       create table hist1(uid int,wid int,primary key(uid,wid),`time` datetime default now());

       id  name   word  time

       create table hist2(id int primary key auto_increment,name varchar(20) not null,word varchar(30),`time` datetime default now());


     * 二级界面 两个界面怎么相互跳转?

       demo.py
## 4. 结构设计 : 使用什么封装,分成几个模块
    客户端   函数
    服务端逻辑   函数
    服务端数据处理   类
    
## 5. 功能划分 和 通信协议设计
    网络通信
    注册
    登录
    查单词
    历史记录
    
##  6. 具体每个功能干什么
    网络通信

    注册
       客户端 :  请求  R name passwd

       服务端 :  验证能否注册
                插入数据库

    登录
    查单词
       客户端 :  请求

        服务端 : 查询单词   插入历史记录

    历史记录
       客户端 :　发送请求　　循环接受历史记录
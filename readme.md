
# Website

Tornado 框架的Uedit富文本编辑器
## Requirement

### 配置文件

- 修改支持文件大小以及文件类型地址: uedit/php/config.json  
- 修改日志索引文件等地方：my.cnf


### 删除所有.pyc文件命令
```
find 路径 -type f -name  "*.pyc"  | xargs -i -t rm -f {}
```

### 结束进程
```
lsof -i:8002 |sed '1d'| awk '{print $2}' | xargs kill -9
```


### 打包命令
```
zip -r zk_css.zip zk_css/
```

### 启动服务
```
nohup python run.py > /dev/null &
```

### 上线注意事项
1. 更改配置文件信息--base里面的配置文件名（my.cnf or ...）  
2. 例如其他用户没有读写权限：  
```
    更改日志权限  
    更改索引权限  
    更改文件目录权限  
```  
3. 修改uploader.py 里面的getFileInfo()类的配置信息, 可在配置文件里面修改  
如果要修改图片的路径， 也是在那个类里面修改print(os.path.join(URL,'static',filename))
```buildoutcfg
# -----<图片的url路径>----- #
[img_url]
host=192.168.2.137
port=8888

```
4. 如果要修改其他内容， 比如允许上传什么样的图片等， 需要修改
```
ueditor/php/config.json
```



### 数据库表结构
##### category
|参数名称         | 参数类型           | 参数说明  |
| ------------- |:-------------:| -----:|
| ID    | int(11) | - |
| Title     | varchar(255)      |   标题 |
| Description | varchar(500)      |    描述 |
| TitleStatus  | int(11) | 状态 |
| CreateTime    | varchar(30) | - |
| UserID    | decimal(28)   | - |


##### text
|参数名称         | 参数类型           | 参数说明  |
|:------------- |:-------------:| -----:|
| ID    | int(11) | - |
| ArticleTitle | varchar(255) | 文章标题 |
| AllHtml | longtext | 富文本编辑器所有的html代码 |
| WriteHtmlContent | longtext | 富文本编辑器所有的html 主要内容 |
| WriteHtml | longtext | 用户写的所有内容 |
| UserID | decimal(28) | - |
| CreateTime | varchar(30) | - |
| ArticleStatus | tinyint(4) | 状态【0删除；1可读；2彻底删除】|
| Version | int | 版本（针对修改而设置的） |
| HomePage| tinyint | 是否放在首页【1放；0不放】|
| Release | tinyint | 发布1 or 草稿2 |
| AllowComment | tinyint | 是否允许评论(1, 0) |
| Top | tinyint | 是否置顶 (1, 0)|
| AllowUserVisit | tinyint | 只允许注册用户访问？(1,0)|
| AllowPassword | tinyint | 密码保护？|
| Password | varchar（255） | 密码 |
| tag | varchar(255) | tag标签 |
| Friends | varchar(255) | 推送给好友的名单 |
| CategoryID | varchar(50) | CategoryID 用于分类默认为空(1.2.3) | 
| HomeImage | varchar(255) | 首页缩略图地址| 
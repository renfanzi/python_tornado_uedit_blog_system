#!/usr/bin/env python
# -*- coding:utf-8 -*-


from controllers.CreateHandlers import *
from controllers.UeditHandlers import *
from controllers.ShowHandlers import *
from controllers.TestHandlers import *
from controllers.SignHandlers import *
from controllers.UpdateHandlers import *

urls = list()

testUrls = [
    (r'/index', MyTestHandler),

    (r'/TestUploadFile', TestUploadFileHandler),

    (r'/TestSignIn', TestSignInHandler),

    (r'/TestSignIn2', TestSignIn2Handler),

    (r'/test.html', TestUploadFileHtmlHandler),

]

createUrls = [
    # -----> 创建项目 <----- #
    (r'/CreateProject', CreateProjectHandler),
]

performsUrls = [
    # 首页
    (r'/index.html', ShowHomeIndexHandler),
]

# -----<富文本编辑器操作-添加文章>----- #
editorUrls = [
    # -----> 富文本编辑器首页 <----- #
    (r'/uedit_index.html', UeditIndexHandler),

    # -----> 富文本编辑器上传文件和图片接口 <----- #
    (r'/upload/', RemotePictureHandler),

    # -----> 添加新文章 <----- #
    (r'/create_article.html', AddArticleHtmlHandler),

]

# -----<文章管理-编辑分类>----- #
articleManageUrl = [
    # -----> 编辑分类 <----- #
    (r'/edit_classify.html', EditClassifyHtmlHandler),

    # -----> 后台管理页面首页 <----- #
    (r'/admin.html', ShowAdminHtmlHandler),

    # -----> 文章目录-我的文章 <----- #
    (r'/article_directories.html', ShowArticleDirectoriesHtmlHandler),

    # -----> 编辑文章 <----- #
    (r'/edit_article.html', UpdateEditArticleHtmlHandler),
]

# -----<登录>----- #
signUrls = [
    # -----<登录页面>----- #
    (r'/login.html', LoginHtmlHandler),

    # -----<登录接口>----- #
    (r'/signin', SignInHandler),
]

showUrls = [

    # -----<查看用户所有文章>----- #
    (r'/show_sample_user_all_article', ShowSampleUserAllArticleHandler),

    # -----<查看单个文章详情>----- #
    (r'/show_single_article', ShowSingleArticleHandler),

    # -----> 查看用户的文章分类目录-创建项目时候用到 <----- #
    (r'/showcategory', ShowCategoryHandler),

    # -----> 查看分页<----- #
    (r'/show_pager', ShowPagerHandler),

    # -----> 查看分页数据<----- #
    (r'/show_pager_data', ShowPagerDataHandler),

]

addUrls = [

    # -----<添加文章分类>----- #
    (r'/add_article_class', AddArticleClassHandler),

    # -----<添加文章到库>----- #后台接口
    (r'/add_article', AddArticleHandler),

]

updateUrls = [

]

deleteUrls = [

]

otherUrls = [
    (r'/.*', ShowOtherHtmlHandler),
]

urls += testUrls + createUrls + performsUrls + editorUrls + articleManageUrl + signUrls

urls += showUrls + addUrls + updateUrls + deleteUrls

# -----<特殊情况放最后>----- #
urls += otherUrls


# 下次可以接口放到一起， html网页接口放到一起
# 最好不要弄混淆
# 接口： add， delete， update， show
# html： 登录， 前台， 后台

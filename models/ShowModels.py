#!/usr/bin/env python
# -*- coding:utf-8 -*-

from common.Base import *


def ShowCategoryModel(UserID):
    sql = """
            SELECT
                *
            FROM
                blog.category
            WHERE
                UserID = %s
            AND TitleStatus = 1;
        """ % UserID
    ret = MyPymysql('notdbMysql')
    data = ret.selectall_sql(sql)
    ret.close()
    return data


def ShowAllArticleModel(UserID):
    sql = """
            SELECT
                  `ID`,
                  `ArticleTitle`,
                  `HomeImage`,
                  `UserID` ,
                  `CreateTime`,
                  `Version`,
                  `HomePage`,
                  `Release`,
                  `AllowComment`,
                  `Top`,
                  `AllowUserVisit`,
                  `AllowPassword`,
                  `Password`,
                  `Tag`,
                  `Friends`,
                  `CategoryID`
            FROM
                blog.text
            WHERE
                UserID = {}
            AND ArticleStatus = 1
            AND `Release` = 1;
        """.format(UserID)
    ret = MyPymysql('notdbMysql')
    data = ret.selectall_sql(sql)
    ret.close()
    return data

def ShowSingleArticleModel(UserID=123456, TextID=None):
    sql = """
            SELECT
                  *
            FROM
                blog.text
            WHERE
                UserID = {} 
            AND `ID`={}
            AND ArticleStatus = 1
            AND `Release` = 1;
        """.format(UserID, TextID)
    ret = MyPymysql('notdbMysql')
    data = ret.selectone_sql(sql)
    ret.close()
    return data


def ShowPagerModel(UserID):
    sql = """
            SELECT
                count(1) as count
            FROM
                blog.text
            WHERE
                UserID = {}
            AND ArticleStatus = 1
            AND `Release` = 1;
        """.format(UserID)
    ret = MyPymysql('notdbMysql')
    data = ret.selectone_sql(sql)
    ret.close()
    return data


class ShowPagerInfoModel():
    def __init__(self, libname="notdbMysql"):
        self.libname = libname
        self.res = MyPymysql(self.libname)

    def ShowPager(self, UserID):
        sql = """
                SELECT
                    count(1) as count
                FROM
                    blog.text
                WHERE
                    UserID = {}
                AND ArticleStatus = 1
                AND `Release` = 1;
            """.format(UserID)
        return self.res.selectone_sql(sql)

    def ShowPagerData(self, UserID, Start, Limit=15):
        sql = """
                SELECT
                    ID, ArticleTitle, HomeImage, CreateTime, Top
                FROM
                    blog.text
                WHERE
                    UserID = {}
                AND ArticleStatus = 1
                AND `Release` = 1 
                ORDER BY
	                `Top` DESC
                Limit {}, {}
                ;
            """.format(UserID, Start, Limit)
        return self.res.selectall_sql(sql)

    def close(self):
        self.res.close()

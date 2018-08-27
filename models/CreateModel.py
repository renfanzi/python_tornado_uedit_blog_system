#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from decimal import Decimal
from common.Base import MyPymysql, MyGuid, my_datetime, my_log


def CreateMetaProj(data):
    sql = """
        INSERT INTO `meta_project`
        SET ProjectID ={}, UserID ={}, ProjectName = '{}',
         ProjectOrgan = '{}',
         ProjectSubject = '{}',
         SubjectField ={}, ProjectLevel ={}, ProjectSource ={}, FundsSource ={}, ProjectSummary = '{}',
         CycleType ={}, CycleSpan = '{}',
         TeamIntroduction = '{}',
         ProjectPublic ={}, ProjectStatus ={}, EditUserID ={};
        """.format(
        data["ProjectID"],
        data["UserID"],
        data["ProjectName"],
        data["ProjectOrgan"],
        data["ProjectSubject"],
        data["SubjectField"],
        data["ProjectLevel"],
        data["ProjectSource"],
        data["FundsSource"],
        data["ProjectSummary"],
        data["CycleType"],
        int(data["CycleSpan"]),
        data["TeamIntroduction"],
        data["ProjectPublic"],
        data["ProjectStatus"],
        data["EditUserID"])
    ret = MyPymysql('metadata')
    ret.idu_sql(sql)
    ret.close()


class MyPagesAndPageDatas():
    """
    from common.util.MyPaging import Pagination

    res = MyPagesAndPageDatas()
    dataCount = res.SelectItemPagesCountModel("2017091710094680349524135490")
    obj = Pagination(dataCount, current_page=52)
    start = obj.start
    end = obj.end
    data = res.SelectItemPagesDataModel(start, end, obj.appear_page)
    print(len(data))

    res.close()
    """

    def __init__(self, libname="notdbMysql"):
        self.libname = libname
        self.res = MyPymysql(self.libname)

    def SelectItemPagesCountModel(self, QuesID):
        selectBaseTableSql = "select DataTableID, DataTableName, DatabaseName from db_metadata.meta_data_table WHERE `QuesID`='{}' AND DataTableStatus=1;".format(
            QuesID)
        self.baseTableData = self.res.selectone_sql(
            selectBaseTableSql)  # {'DataTableName': '', 'DataTableID': '', 'DatabaseName': ''}

        dataSql = """select count(1) as count from {}.{}""".format(self.baseTableData["DatabaseName"],
                                                                   self.baseTableData["DataTableName"])

        result = self.res.selectone_sql(dataSql)
        return result["count"]

    def SelectItemPagesDataModel(self, start, end, appear_page):
        sql = """select `StartTime`, `EndTime`, `NominalTime`, `SpaceName`, `Topic`, `Index`, `DataValue`, `DataDescription` from {}.{} limit {}, {};""".format(
            self.baseTableData["DatabaseName"],
            self.baseTableData["DataTableName"],
            start,
            appear_page)
        result = self.res.selectall_sql(sql)
        return result

    def close(self):
        self.res.close()


def AddArticleClassModel(title, description, UserID):
    sql = """
        INSERT INTO blog.category
        SET Title ="%s", 
            Description ="%s", 
            TitleStatus=1, 
            CreateTime="{}",
            UserID={}
        """.format(my_datetime.str_datetime(), UserID)
    ret = MyPymysql('notdbMysql')
    value = (title, description)
    ret.idu_sql(sql, value=value)
    ret.close()


def AddArticleModel(info):
    sql = """
            INSERT INTO `blog`.`text`
            SET
                `ArticleTitle`="%s",
                `AllHtml`="%s",
                `WriteHtmlContent`="%s",
                `WriteHtml`="%s",
                `ArticleStatus`=%s,
                `Version`=%s,
                `HomePage`=%s,
                `Release`=%s,
                `AllowComment`=%s,
                `Top`=%s,
                `AllowUserVisit`=%s,
                `AllowPassword`=%s,
                `Password`="%s",
                `Tag`="%s",
                `Friends`="%s",
                `CategoryID`="%s",
                `UserID`=%s,
                `CreateTime`=%s,
                `HomeImage`="%s"
    """
    ret = MyPymysql('notdbMysql')
    value = (
        info["ArticleTitle"],  # ArticleTitle
        info["AllHtml"],  # AllHtml
        info["WriteHtmlContent"],  # WriteHtmlContent
        info["WriteHtml"],  # WriteHtml

        1,  # ArticleStatus
        1,  # Version
        int(info["HomePage"]),  # HomePage
        int(info["Release"]),  # Release

        int(info["AllowComment"]),  # AllowComment
        int(info["Top"]),  # Top
        1,  # AllowUserVisit
        int(info["AllowPassword"]),  # AllowPassword

        info["Password"],  # Password
        info["Tag"],  # tag
        info["Friends"],  # Friends
        info["CategoryID"],  # CategoryID
        info["UserID"],
        info["CreateTime"],
        info["HomeImage"],
    )
    ret.idu_sql(sql, value=value)
    ret.close()
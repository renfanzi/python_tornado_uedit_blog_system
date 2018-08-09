#!/usr/bin/env python
# -*- coding:utf-8

# -----<分页>----- #


class Pagination:
    """
    explain:
        obj = Pagination(1000, 20, 50)
        print(obj.start)
        print(obj.end)
        obj.item_pages --> 求分页的页码
    all_item :need the query library to count
    """
    """
    all_item: 总count
    current_page: 你的页数、
    appear_page： 每页多少条数据
    """

    def __init__(self, all_item, current_page=1, appear_page=15):
        try:
            self.appear_page = appear_page
            self.int = int(current_page)
            self.all_item = all_item
            page = self.int
        except:
            self.all_item = 0
            page = 1
        if page < 1:
            page = 1

        all_pager, c = divmod(all_item, self.appear_page)
        if c > 0:
            all_pager += 1

        self.current_page = page
        self.all_pager = all_pager

    @property
    def start(self):
        return (self.current_page - 1) * self.appear_page

    @property
    def end(self):
        return self.current_page * self.appear_page

    @property
    def item_pages(self):
        all_pager, c = divmod(self.all_item, self.appear_page)
        if c > 0:
            all_pager += 1
        return 1, all_pager + 1


if __name__ == '__main__':
    obj = Pagination(14, 1)
    print(obj.start)
    print(obj.end)
    print(obj.item_pages)

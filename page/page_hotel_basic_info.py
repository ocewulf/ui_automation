#!/usr/bin/env python
# -*- encoding = 'utf-8' -*-
"""
@Author     : ocewulf
@Version    :  1.0
@Modify Time: 2022/5/7 18:08 
"""
import page
from base.base import Base


class PageHotelBasicInfo(Base):
    # 获取列表问卷编号
    def page_get_survey_num(self):
        return self.base_get_text(page.survey_num)
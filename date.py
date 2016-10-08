# -*- coding:utf-8 -*-

import calendar
from datetime import datetime


class DateUtils(object):
    U'''
        Recupera todos os domingos de um determinado mês e ano em formto "Date" <datetime>
    '''
    def get_month_sundays(self, year, month):
        list_sunday_date = []
        list_sunday = [week[-1] for week in calendar.monthcalendar(year, month) if week[-1] > 0]
        for sunday in list_sunday:
            sunday_date = datetime(year=year, month=month, day=sunday).date()
            list_sunday_date.append(sunday_date)
        return list_sunday

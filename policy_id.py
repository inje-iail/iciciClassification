import os
import time
from pdf2image import convert_from_path
import requests
import time
import json
import re
from dateutil.parser import parse
import calendar


def policy_card(text_json):
    s = ""
    for i in range(len(text_json)):
        s = s + " " + text_json[i].get("text")
    original_string = s
    s = s.replace(':',' ')
    s = s.replace('Company Name', 'CompanyName')
    s = s.split(' ')
    temp = []
    for item in s:
        if item != '':
            temp.append(item)
    s = temp
    name = ''
    for i in range(len(s)):
        if s[i].upper() == 'NAME':
            for j in range(5):
                if s[i+j+1].isupper():
                    name = name + ' ' + s[i+j+1]
                else:
                    if len(name) != 0:
                        break
    name = name.strip()
    policy_no = ''
    for item in s:
        if len(item) > 15 and '/' in item and re.match('^.*000$',item):
            policy_no = item
    gender = ''
    for item in s:
        if item.upper() in ['MALE','FEMALE']:
            gender = item
            break
    age = ''
    for i in range(len(s)):
        if s[i].upper() == 'AGE':
            for j in range(5):
                if re.match('^[1-9][0-9]$', s[i+j+1]):
                    age = s[i+j+1]
                    break
    card_no = ''
    for i in range(len(s)):
        if s[i].upper() == 'CARD' and s[i+1].upper() == 'NO':
            card_no = s[i+2]
            if len(card_no) <= 2:
                card_no = card_no + s[i+3]
            break
    emp_id = ''
    for i in range(len(s)):
        if s[i].upper() == 'EMP' and s[i+1].upper() == 'ID':
            emp_id = s[i+2]
            break
    dates = []
    for item in s:
        try:
            if re.match(
                    '^([0-9][0-9]?\-?\s?[A-Z][A-Za-z]{2}\s?\-?\s?[0-9]?[0-9]?[0-9]{2})$',item) or re.match('^[0-9][0-9]?\-[0-9]{2}\-[0-9]{4}$',item):
                temp = parse(item)
                print(item)
                dates.append(temp)
        except:
            pass
    to_date = ''
    from_date = ''
    DOB = ''
    dates = set(dates)
    dates = list(dates)
    print("----------",dates)
    dates = sorted(dates)
    for i in range(len(dates)):
        date1 = dates[i]
        for j in range(i + 1, len(dates)):
            date2 = dates[j]
            if date2.year - date1.year == 1:
                from_date = str(date1.day) + '-' + str(calendar.month_abbr[date1.month]).upper() + '-' + str(date1.year)
                to_date = str(date2.day) + '-' + str(calendar.month_abbr[date2.month]).upper() + '-' + str(date2.year)
    for date in dates:
        if date.year <= 1999:
            DOB = str(date.day) + '-' + str(calendar.month_abbr[date.month]).upper() + '-' + str(date.year)
    if len(DOB) != 0 and len(dates) == 2:
        to_date = str(dates[1].day) + '-' + str(calendar.month_abbr[dates[1].month]).upper() + '-' + str(dates[1].year)
    result = {
        'name' : name,
        'policy_no' : policy_no,
        'gender' : gender,
        'age' : age,
        'card_no' : card_no,
        'emp_id' : emp_id,
        'DOB' : DOB,
        'from_date' : from_date,
        'to_date' : to_date,
    }
    return result


# f = open(r"F:\iAssist_Projects\iciciClassification\all_bill.json", "r")
#
# # Reading from file
# json1 = json.loads(f.read())
# text_json = json1["e287b96e-2f33-4fdc-a41a-d89d50ef38961.jpg"]
# policy_card(text_json)
import re
from w3lib import html
from datetime import datetime, timezone, timedelta
from orv2.spiders.reg import WT_REG, DM_REG, SP_REG, DT_REG, DAY_REG, EMP_REG, EMA_REG

def info_handler(response):
    info_dic = {"DV": "", "WT": -1, "DM": "", "SP": -1, "TM": "", "CB": "", "DO": []}
    infos = [(a, b) for (a, b) in zip(response.xpath("div[1]/text()").getall(), response.xpath("div[2]/text()").getall())]
    for info in infos:
        if info[0] == "Date of Visit":
            info_dic["DV"] = date_handler(info[1])
        elif info[0] == "Waiting Time":
            match = WT_REG.search(info[1])
            if match:
                info_dic["WT"] = match[0]
            match = DM_REG.search(info[1])
            if match:
                info_dic["DM"] = match[0]
        elif info[0] == "Dining Method":
            info_dic["DM"] = info[1]
        elif info[0] == "Spending Per Head":
            match = SP_REG.search(info[1])
            if match:
                info_dic["SP"] = match[0]
            match = DM_REG.search(info[1])
            if match:
                info_dic["TM"] = match[0]
        elif info[0] == "Type of Meal":
            info_dic["TM"] = info[1]
        elif info[0] == "Celebration":
            info_dic["CB"] = info[1]
        elif info[0] == "Dining Offer":
            info_dic["DO"] = info[1].split(",")
    return info_dic.items()
    

def date_handler(date_texts):
    match = DT_REG.search(date_texts)
    if match:
        return match[0]
    else:
        current = datetime.today().astimezone(timezone(timedelta(seconds=28800)))
        if date_texts == "Today":
            return current.date().isoformat()
        else:
            match = DAY_REG.search(date_texts)
            if match:
                return (current - timedelta(days=int(match[0]))).date().isoformat()
            else:
                return (current - timedelta(days=1)).date().isoformat()

def html_handler(html_text):
    text = EMA_REG.sub("]", EMP_REG.sub("[", html_text))
    text = html.remove_tags_with_content(text, which_ones=('a', 'br'))
    text = html.replace_escape_chars(text, replace_by=" ")
    text = html.strip_html5_whitespace(html.replace_tags(text, " "))
    return " ".join(text.split())
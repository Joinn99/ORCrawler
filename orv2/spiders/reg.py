import re

EMOJI_REG = re.compile(u"[\U000000A9|\U000000AE|\U0000203C|\U00002049|\U00002122|\U00002139|\U00002194-\U00002199|\U000021A9-\U000021AA|\U0000231A-\U0000231B|\U00002328|\U000023CF|\U000023E9-\U000023F3|\U000023F8-\U000023FA|\U000024C2|\U000025AA-\U000025AB|\U000025B6|\U000025C0|\U000025FB-\U000025FE|\U00002600-\U00002604|\U0000260E|\U00002611|\U00002614-\U00002615|\U00002618|\U0000261D|\U00002620|\U00002622-\U00002623|\U00002626|\U0000262A|\U0000262E-\U0000262F|\U00002638-\U0000263A|\U00002640|\U00002642|\U00002648-\U00002653|\U0000265F-\U00002660|\U00002663|\U00002665-\U00002666|\U00002668|\U0000267B|\U0000267E-\U0000267F|\U00002692-\U00002697|\U00002699|\U0000269B-\U0000269C|\U000026A0-\U000026A1|\U000026AA-\U000026AB|\U000026B0-\U000026B1|\U000026BD-\U000026BE|\U000026C4-\U000026C5|\U000026C8|\U000026CE-\U000026CF|\U000026D1|\U000026D3-\U000026D4|\U000026E9-\U000026EA|\U000026F0-\U000026F5|\U000026F7-\U000026FA|\U000026FD|\U00002702|\U00002705|\U00002708-\U0000270D|\U0000270F|\U00002712|\U00002714|\U00002716|\U0000271D|\U00002721|\U00002728|\U00002733-\U00002734|\U00002744|\U00002747|\U0000274C|\U0000274E|\U00002753-\U00002755|\U00002757|\U00002763-\U00002764|\U00002795-\U00002797|\U000027A1|\U000027B0|\U000027BF|\U00002934-\U00002935|\U00002B05-\U00002B07|\U00002B1B-\U00002B1C|\U00002B50|\U00002B55|\U00003030|\U0000303D|\U00003297|\U00003299|\U0001F004|\U0001F0CF|\U0001F170-\U0001F171|\U0001F17E-\U0001F17F|\U0001F18E|\U0001F191-\U0001F19A|\U0001F201-\U0001F202|\U0001F21A|\U0001F22F|\U0001F232-\U0001F23A|\U0001F250-\U0001F251|\U0001F300-\U0001F321|\U0001F324-\U0001F393|\U0001F396-\U0001F397|\U0001F399-\U0001F39B|\U0001F39E-\U0001F3F0|\U0001F3F3-\U0001F3F5|\U0001F3F7-\U0001F4FD|\U0001F4FF-\U0001F53D|\U0001F549-\U0001F54E|\U0001F550-\U0001F567|\U0001F56F-\U0001F570|\U0001F573-\U0001F57A|\U0001F587|\U0001F58A-\U0001F58D|\U0001F590|\U0001F595-\U0001F596|\U0001F5A4-\U0001F5A5|\U0001F5A8|\U0001F5B1-\U0001F5B2|\U0001F5BC|\U0001F5C2-\U0001F5C4|\U0001F5D1-\U0001F5D3|\U0001F5DC-\U0001F5DE|\U0001F5E1|\U0001F5E3|\U0001F5E8|\U0001F5EF|\U0001F5F3|\U0001F5FA-\U0001F64F|\U0001F680-\U0001F6C5|\U0001F6CB-\U0001F6D2|\U0001F6D5|\U0001F6E0-\U0001F6E5|\U0001F6E9|\U0001F6EB-\U0001F6EC|\U0001F6F0|\U0001F6F3-\U0001F6FA|\U0001F7E0-\U0001F7EB|\U0001F90D-\U0001F93A|\U0001F93C-\U0001F945|\U0001F947-\U0001F971|\U0001F973-\U0001F976|\U0001F97A-\U0001F9A2|\U0001F9A5-\U0001F9AA|\U0001F9AE-\U0001F9CA|\U0001F9CD-\U0001F9FF|\U0001FA70-\U0001FA73|\U0001FA78-\U0001FA7A|\U0001FA80-\U0001FA82|\U0001FA90-\U0001FA95]")
WT_REG = re.compile(r"^[0-9]+")
DM_REG = re.compile(r"(?<=\()[A-Z|a-z]+(?=\))")
SP_REG = re.compile(r"(?<=^\$)[0-9]+")
DT_REG = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")
DAY_REG = re.compile(r"[1-7](?= day)")
EMP_REG = re.compile(r"<div.+?(re-icon-)")          # Emoji Previous
EMA_REG = re.compile(r"(?<=[a-z|0-9])\"></div>")    # Emoji After
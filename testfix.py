from dateutil.parser import parse
def change_date_format(x):
    res = []

    for i in x:
        if "/" in i or "-" in i:
            p = parse(i)
            res.append(p.strftime('%Y%m%d'))
    return res


print(change_date_format(["2019/03/30", "15/12/2006", "11-15-2012", "20130730"]))

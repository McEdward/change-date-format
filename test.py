def change_date_format(x):
    res = []
    for i in x:
        if len(i) == 10:
            ans = ""
            if "/" in i and i.find("/") == 4 and i[7] == "/":
                ans += i[:4]
                ans += i[5:7]
                ans += i[8:]
                res.append(ans)
            elif "/" in i and i.find("/") == 2 and i[5] == "/":
                ans += i[6:]
                ans += i[3:5]
                ans += i[:2]
                res.append(ans)
            elif "-" in i and i.find("-") == 2 and i[5] == "-":
                ans += i[6:]
                ans += i[3:5]
                ans += i[:2]
                res.append(ans)
    return res

print(change_date_format(["2019/03/30", "15/12/2006", "11-15-2012", "20130730"]))

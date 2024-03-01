"""
dict练习
升职加薪
如下员工信息，用字典完成数据记录
用for循环对所有级别为1级的员工，级别上升一级，薪水增加1000元
姓名      部门      工资       级别
AZ      科技部     3000        1
YX      市场部     5000        2
DVX     市场部     7000        3
TX      科技部     4000        1
WJ      市场部     6000        2
"""
mydict = {
    'AZ': {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    'YX': {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    'DVX': {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    'TX': {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    'WJ': {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(f"员工信息记录表{mydict}")
for name in mydict:
    if mydict[name]["级别"] == 1:
        employee_dict = mydict[name]
        employee_dict["级别"] = 2
        employee_dict["工资"] += 1000
        mydict[name] = employee_dict
print(f"员工升职加薪后的结果{mydict}")

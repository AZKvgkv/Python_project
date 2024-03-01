# 读取一个文件，并统计该文件里面的 itheima 共出现的次数
# 方式一
'''
with open('word.txt') as f:
    count = (f.read()).count('itheima')
print(f"该文件中的 itheima 共出现了{count}次")
'''


# 方式二
counts = 0
with open("word.txt") as file:
    for line in file:
        line = line.strip()     # 去除开头和结尾的空格及换行符
        words = line.split(" ")
        for word in words:
            if word == 'itheima':
                counts += 1
print(f"文件中的 itheima 一共出现了{counts}次!")




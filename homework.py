# 1.添加学生
#
# 2.查找学生
#
# 3.删除学生
#
# q.退出系统



print('aaa'.isnumeric(),'123'.isnumeric())
stu_inf = [{'name':'zhangsan', 'age':22, 'phone':12457689876},
           {'name':'lishi', 'age':22, 'phone':12457689876}]
print('1. add student\'s messages;\n2. looking for student\'s message;'
      '\n3. delete student\'s message;\nq. exit system.\n============')
# stu_inf = student information；ch_num = choice number
# 1.添加学生
flag = True
x = 0
while flag:
    # 输入选项进行操作
    ch_num = input('\nPlease enter the number for the option:')

    # 退出系统
    if ch_num == 'q':
        print('You\'re exit system')
        break
    ch_num = int(ch_num)

    # 添加学生信息
    if ch_num == 1:
        dict1 = {}
        name = input('Please enter the student\'s name:')
        dict1['name'] = name

        age = input('Please enter the student\'s age:')
        if age.isnumeric() == False:
            print('Age is integer,please enter gain')
            continue
        else:
            dict1['age'] = age


        phone = int(input('Please enter the studen\'s phone:'))
        dict1['phone'] = phone

        stu_inf.append(dict1)

    # 查找学生信息
    elif ch_num == 2:
        name = input('Please enter the student\'s name:')
        for item1 in stu_inf:
            if item1['name'] == name:
                for key in item1:
                    print(key, item1[key])
                break
        else:
            print('%s is out of system' % (name))


    # 删除学生信息
    elif ch_num == 3:
        name = input('Please enter the student\'s name:')
        for item2 in stu_inf:
            if item2['name'] == name:
                print('Please enter the student\'s number: %d to confirm deletion'


                      % (stu_inf.index(item2)))
                num = int(input())
                if num == stu_inf.index(item2):
                    message = stu_inf.pop(num)
                    print(message, 'is deleted')
                else:
                    break
        else:
            print('%s is not in the system,please enter again.' % (name))

    else:   # 提示输入错误
        print('enter error')

    # 限制对系统的操作次数
    x += 1
    if x > 5:
        flag = False
        print('Input up to 6 times,exit the system')








"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

"""

from random import randint
from os import system


def change_type(str):
    if type(str) == type('12312'):
        if str.isdigit():
            result = int(str)
            # print(result,'是整数 类型是',type(result))
            return result
        else:
            if str.count(".") == 1 and not str.startswith(".") and not str.endswith("."):
                # 整数部分
                integer = str.split('.')[0]
                decimal = str.split('.')[1]
                if integer.isdigit() & decimal.isdigit():
                    result = float(str)
                    # print(result,"是小数 类型是",type(result))
                    return result
    else:
        # print("输入的变量不是字符串类型")
        result = str
        return result


def if_strin(money):
    if '.' in str(money) and '0' in str(money):
        moneystr = str(money)
        money = int(moneystr.split('.')[0])
        print(money)
    return money


system('cls')
money = 1000
while money > 0:
    print('你的总资产为:', money)
    needs_go_on = False
    while True:
        debt = input('请下注: ')
        resultone = change_type(debt)
        if type(resultone) == type(123) or type(resultone) == type(3.1415926):
            if 0 < resultone <= money:
                break
            else:
                print('资产不足，请重新下注!!!')
        else:
            print('输入类型错误，请重新输入!!!')
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家胜!')
        money += resultone
        if type(money) == type(1234.4) and '0' in str(money).split('.')[1]:
            money = if_strin(money)
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!')
        money -= resultone
        money = if_strin(money)
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print('庄家胜')
            money -= resultone
            money = if_strin(money)
        elif current == first:
            print('玩家胜')
            money += resultone
            money = if_strin(money)
        else:
            needs_go_on = True
if money <= 0:
    print('你破产了, 游戏结束!')

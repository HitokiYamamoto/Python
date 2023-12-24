# int = 整数
# float = 小数
# str = 文字列
# bool = 真偽値

#割り算プログラム
'''
price = input('料金を入力 >>')
price = int(price)
number = input('人数を入力 >>')
number = int(number)
payment = price / number
payment = int(payment)
print('お支払いは' + str(payment) + '円です')
'''


price = int(input('料金を入力 >>'))
number= int(input('人数を入力 >>'))
payment = int(price / number)
print('お支払いは{}円です'.format(payment))

name = '松田翔太'
age = 23
height = 175.6
print(f'私の名前は{name}で、年齢は{age}歳で、\n'
      f'身長は{height}cmです')

hp, maxHP = 80, 100
print(f'{hp } / {maxHP}')
print(f'{hp = } / {maxHP = }')
print(f'{hp / maxHP = }')
'''
print('半径が3cmの円の直径は、')
print(3 * 2)
print('その円の円周率の長さは、直径×円周率で求まるため、')
print(3 * 2 * 3.14)
'''

print('半径が3cmの円の直径は、')
dia = 3 * 2
print(dia)
print('その円の円周の長さは、')
print(dia * 3.14)

#変数の上書き
count = 3
print('今日はカレーを食べた回数は')
print(count)
count = 5
print('嘘。本当は')
print(count)

#予約語

import keyword
print(keyword.kwlist)

#キーボード入力値の代入

name = input('あなたの名前を入力してください')
print('おお' + name + 'よ、そなたが来るのを待っておったぞ！')


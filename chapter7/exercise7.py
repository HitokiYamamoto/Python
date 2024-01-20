# 次の機能を持つプログラムを、組み込み関数を使ってそれぞれ作成してください。
# ただしいずれも必ず指定の数値が入力されることを前提とします。
# (1)入力された3つの整数のうち、大きい値を表示する。
# (2)円周率3.141592について、小数点以下第１位から第５位を四捨五入した値をそれぞれ表示する。


num1 = input('1つ目の整数を入力してください >>')
num2 = input('2つ目の整数を入力してください >>')
num3 = input('3つ目の整数を入力してください >>')

max_value = max(num1, num2, num3)
print('入力された整数のうち、大きい値は:', max_value)

pi_value = 3.141592

rounded_pi_1 = round(pi_value, 1)
rounded_pi_2 = round(pi_value, 2)
rounded_pi_3 = round(pi_value, 3)
rounded_pi_4 = round(pi_value, 4)
rounded_pi_5 = round(pi_value, 5)

print("小数点以下第１位から第５位までを四捨五入した値:")
print("第１位:", rounded_pi_1)
print("第２位:", rounded_pi_2)
print("第３位:", rounded_pi_3)
print("第４位:", rounded_pi_4)
print("第５位:", rounded_pi_5)
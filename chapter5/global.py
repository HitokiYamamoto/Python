# global文を用いてグローバル変数に代入する

name = '松田'
def change_name():
    global name
    name = '浅木'
def hello():
    print('こんにちは' + name + 'さん')

change_name()
hello()


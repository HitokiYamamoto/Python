# 2つの戻り値を返す
# def plus_and_minus(a, b):
#     return (a + b, a - b)

# (next, prev) = plus_and_minus(1978, 1)

# print(next, prev)

# おやつも食べた日のeat関数の呼び出し(可変長引数を利用)

def eat(breakfast, lunch, dinner='カレー', *desserts):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')
    for d in desserts:
        print(f'おやつに{d}を食べました')

eat('トースト', 'パスタ', 'カレー', 
    'アイス', 'チョコ', 'カレー')
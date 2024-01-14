# def hello():
#     print('こんにちは。工藤です。')
# hello()

# 引数と戻り値
# def hello(name):
#     print(f'こんにちは。{name}です。')
# hello('浅木')
# hello('松田')

# 複数の引数を渡す
# def profile(name, age, hobby):
#     print(f'私の名前は{name}です。')
#     print(f'年齢は{age}です。')
#     print(f'趣味は{hobby}です。')
# profile('浅木', 24, 'カフェ巡り')

# 戻り値

# def plus(x, y):
#     answer = x + y
#     return answer

# answer = plus(100, 50)
# print(f'足し算の答えは{answer}です')

# 関数を利用して試験結果を計算する

def input_scores(name):
    print(f'{name}さんの試験結果を入力してください')
    network = int(input('ネットワークの得点? >>'))
    database = int(input('データベースの得点? >>'))
    security = int(input('セキュリティの得点? >>'))
    scores = [network, database, security]
    return scores

def calc_average(scores):
    avg = sum(scores) / len(scores)
    return avg

def output_result(name, avg):
    print(f'{name}さんの平均点は{avg}です')

asagi_scores = input_scores('浅木')
matsuda_scores = input_scores('松田')

asagi_avg = calc_average(asagi_scores)
matsuda_avg = calc_average(matsuda_scores)

output_result('浅木', asagi_avg)
output_result('松田', matsuda_avg)
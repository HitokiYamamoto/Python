# 次の動作を順に行うプログラムをwhile文を用いて作成してください
# 変数countを任意の値で初期化する
# 画面に「カレーを召し上がれと表示する」
# 画面に「⚪︎皿のカレーを食べました」と表示する（⚪︎には食べた皿数が入る）
# 画面に「おかわりはいかがですか？(y/n) >>」と表示する。
# yが入力されたら、変数　countの値を1増やして(3)へ戻る。
# nが入力されたら、「ごちそうさまでした」と表示して終了する。

# count = 0
# print('カレーを召し上がれ')

# while True:
#     print(f'{count + 1}皿のカレーを食べました')
#     seconds = input('おかわりはいかがですか？(y/n) >>')

#     if seconds == 'y':
#         count += 1
#     elif seconds == 'n':
#         print('ごちそうさまでした')
#         break
#     else:
#         print('yかnで再度入力してください')

# 「10、９、8、・・・・・・、２、１、Lift off！」のようなカウントダウンを行うプログラムを
# for文とrange関数を用いて作成してください。
# なお、print関数にendオプションをつけると、改行せずに文字列を表示できます。

# for i in range(10, 0, -1):
#     print(i, end=',')
# print('Lift off!')

# 九九の計算をするプログラムを、for文を用いて作成する
# (1)のプログラムについて、奇数の段のみ計算するようにcontinue文を用いて変更する
# (2)のプログラムについて、掛け算の答えが50を超えたらその段の計算を中止し、次の段の計算へ進むように変更する。

# 奇数の段のかけ算で、かつ50を超えた場合は中止
for i in range(1, 10, 2):
    # 9の段以外の場合
    if i != 9:
        for j in range(1, 10):
            result = i * j

            if result > 50:
                break

            print(f'{i} × {j} = {result}')
    else:
        # 9の段のかけ算で、かつ50を超えた場合は中止
        for j in range(1, 10):
            result = i * j

            if result > 50:
                break

            print(f'{i} × {j} = {result}')
        break




 
# 練習2-1

## 次の各要件のために用いるコンテナとして、一般的に最も妥当と考えられるものを、
## リスト、セット、ディクショナリから選んでください。
## ただし、コンテナはネストせず1つのみを利用するものとします。

## (1) 47都道府県の「都道府県名と人口」
## (2) 解析に用いるための過去28日分の「1日あたりのWebサイトアクセス数」
## (3) 「北」や「南」といった4つの方角
## (4) この世に存在する「メジャーなプログラミング言語の名称」(PythonやRubyなど)
## (5) ある航空機の200座席の予約状態(0なら空き、1なら予約済み)


# 練習2-2

## キーボードから国語・算数・理科・社会・英語の5つの試験結果の点数を
## ユーザーに入力してもらい、その合計点と平均点を表示するプログラムを作成してください。


# ユーザーからの入力
# kokugo = int(input("国語の点数を入力してください: "))
# sansu = int(input("算数の点数を入力してください: "))
# rika = int(input("理科の点数を入力してください: "))
# shakai = int(input("社会の点数を入力してください: "))
# english = int(input("英語の点数を入力してください: "))

# 合計点の計算
# total = kokugo + sansu + rika + shakai + english

# 平均点の計算
# average = total / 5

# 結果の表示
# print(f"合計点: {total}")
# print(f"平均点: {average}")


# 練習2-3 

## 次のような仕様の相性診断プログラムを作成してください。

## (1) 1人目の趣味を5つ格納したセットを準備する。
## (2) 2人目の趣味を5つ格納したセットを準備する。
## (3) 「心の準備ができたらEnterキーを押してください」と表示して入力を待つ。
## (4) 2人の趣味の「積集合の要素数÷和集合の要素数」を計算し、0~100%の「相性度」として表示する。


# 1人目の趣味を入力
hobbies1 = set(input("1人目の趣味を5つ入力してください（スペースで区切って）: ").split())

# 2人目の趣味を入力
hobbies2 = set(input("2人目の趣味を5つ入力してください（スペースで区切って）: ").split())

# ユーザーの入力待ち
input("心の準備ができたらEnterキーを押してください...")

# 相性度の計算
intersection_count = len(hobbies1.intersection(hobbies2))
union_count = len(hobbies1.union(hobbies2))
compatibility = (intersection_count / union_count) * 100

# 結果の表示
print(f"相性度: {compatibility:.2f}%")

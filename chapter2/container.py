# コンテナの相互変換

scores = {'network':60, 'database':80, 'security':60}
members = ['松田', '浅木', '工藤']
print(tuple(members))
print(list(scores))
print(set(scores.values()))

# コンテナのネスト

## コンテナの中にディクショナリをネスト

matsuda_scores = {'network':60, 'database':80, 'security':50}
asagi_scores = {'netword':80, 'database':75, 'security':92}
member_scores = {
  '松田': matsuda_scores,
  '浅木': asagi_scores
}

## ディクショナリの中にセットをネスト

member_hobbies = {
  '松田': {'SNS', '麻雀', '自転車'},
  '浅木': {'麻雀', '食べ歩き', '数学', '数学', '数学'} # 数学は1つのみ登録される
}

#　全員の趣味を表示する
print(member_hobbies)
# 松田くんの趣味一覧を表示する
print(member_hobbies['松田'])
# 浅木さんの趣味一覧を表示する
print(member_hobbies['浅木'])


# 2次元リストの例

a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b] # aを0番目,bを1番目とする2次元リストcを定義

print(c) # リストc全体を参照
print(c[0]) # リストcの0番目(リストa)だけを参照
print(c[1][2]) # リストcの1番目(リストb)の2番目だけを参照

# 集合演算

## 松田くんの趣味と浅木さんの趣味の共通点を探す

common_hobbies = member_hobbies['松田'] & member_hobbies['浅木']
print(common_hobbies)

# 4つの集合演算

A = {1, 2, 3, 4}
B = {2, 3, 4, 5}

print(A | B) # 和集合
print(A & B) # 積集合
print(A - B) # 差集合
print(A ^ B) # 対称差
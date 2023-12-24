members = ['工藤', '松田', '浅木']
print(members)
print(members[0])

# ネットワーク、データベース、セキュリティ試験の点数

scores = [88, 90, 95]
total = sum(scores)
print(f'合計{total}点')

# リストの合計値と平均値を求める

scores = [88, 90, 95]
total = sum(scores)
avg = total / len(scores)
print(f'合計{total}点, 平均{avg}点')

# リスト要素の追加・削除・変更

## リストに要素を追加

members.append('菅原')
members.append('湊')
members.append('朝香')
print(members)

## リストから要素を削除

members.remove('松田')
print(members)

## リストの要素を変更

members[2] = '山本'
print(members)

# スライスによる範囲指定

a = [10, 20, 30, 40, 50]
print(a[1:3]) # 添え字が1以上3未満の要素
print(a[2:])  # 添え字が2以上の全ての要素
print(a[:3])  # 添え字が3未満のすべての要素

## 負の数による指定

print(a[-1]) # 末尾の要素を参照
print(a[-2]) # 末尾から2番目の要素を参照



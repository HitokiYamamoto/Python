# タプル

scores = (70, 80,55)
print(scores)
print(scores[0])
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')

 # 要素数1のタプル

members = ('松田',) # タプル定義に記述する値の後ろにカンマを付ける
print(type(members))

# セット

scores = {70, 80, 55, 80}
scores.add(80)
print(scores)
print(f'要素数は{len(scores)}')
print(f'合計は{sum(scores)}')
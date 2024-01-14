# 文字列のメソッドを活用した血液型占い
# user_info = input('名前と血液型をカンマを区切って1行で入力 >>')
# [name, blood] = user_info.split(',')
# blood = blood.upper().strip()
# print(f'{name}さんは{blood}型なので大吉です')

# 勇者を表すクラスの定義と利用
# class Hero:
#     name = '松田'
#     hp = 100
#     def sleep(self, hours):
#         print(f'{self.name}は{hours}時間寝た!')
#         self.hp += hours

# print('スッキリファンタジーXII 〜金色の理想郷〜')
# h = Hero()
# h.sleep(3)
# print(f'{h.name}のHPは現在{h.hp}です')

# オブジェクトのidentityを確認

# scores1 = [80, 40, 50]
# scores2 = [80, 40, 50]
# print(f'scores1のidentity: {id(scores1)}')
# print(f'scores2のidentity: {id(scores2)}')

# if scores1 == scores2:
#     print('scores1とscores2は同じ内容です')
# else:
#     print('scores1とscores2は違う内容です')

# if id(scores1) == id(scores2):
#     print('scores1とscores2は同じ存在です')
# else:
#     print('scores1とscores2は違う存在です')

# 防御的コピーを用いて参照の悪影響を防ぐ

def add_suffix(names):
    for i in range(len(names)):
        names[i] = names[i] + 'さん'
    return names

before_names = ['松田', '浅木', '工藤']
copied_names = list(before_names)  
after_names = add_suffix(copied_names)
print('さん付け後：' + after_names[0])
print('さん付け前：' + before_names[0])

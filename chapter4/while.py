# 羊を数えるのを3回繰り返す
# count = 0
# while count < 3:
#     count += 1
#     print(f'羊が{count}匹')
# print('おやすみなさい')

# 眠るまで羊を数えるのを繰り返す
# is_awake = True
# count = 0
# while is_awake == True:
#     count += 1
#     print(f'羊が{count}匹')
#     key = input('もう眠りそうですか?(y/n) >>')
#     if key == 'y':
#         is_awake = False
# print('おやすみなさい')

# 繰り返しを使って得点リストを作成する
# count = 0
# student_num = int(input('学生の数を入力 >>'))
# score_list = list()
# while count < student_num:
#     count += 1
#     score = int(input(f'{count}人目の試験の得点を入力'))
#     score_list.append(score)
# print(score_list)
# total = sum(score_list)
# avg = total / student_num
# print(f'平均点は{avg}点です')

# リストの全要素を繰り返し参照する
scores = [80, 20, 75, 60]
count = 0
while count < len(scores):
    if scores[count] >= 60:
        print('合格')
    else:
        print('不合格')
    count += 1
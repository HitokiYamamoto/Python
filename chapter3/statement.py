# if文

# name = input('あなたの名前を教えてください >>')
# food = input(f'{name}さんの好きな食べ物を教えてください >>')
# if food == 'カレー':
#   print('素敵です。カレーは最高ですよね!!')
# else:
#   print(f'私も{food}が好きですよ')

# 条件式

# name = input('あなたの名前を教えてください >>')
# print(f'{name}さん、こんにちは')
# food = input(f'{name}さんの好きな食べ物を教えてください')
# if 'カレー' in food:
#     print('素敵です。カレーは最高ですよね！！')
# else:
#     print(f'私も{food}が好きですよ')

# scores = [80, 100, 20, 60]
# if 100 in scores:
#     print('100転満点の試験があったんですね。おめでとう!')
# else:
#     print('次はどれか1つでも100点満点を取ろう')


# scores = {'network':60, 'database':80, 'security':50}

# key = input('追加する科目名を入力してください')
# if key in scores:
#     print('すでに登録済みです')
# else:
#     data = int(input('得点を入力してください>>'))
#     scores[key] = data
# print(scores)


# 真偽値

# score = int(input('試験の点数を入力 >>'))
# print(score >= 60)

# if-else構文

# score = int(input('試験の点数を入力してください >>'))
# if score < 0 or score > 100:
#     print('異常な得点です')
#     print('入力し直してください')
# elif score >= 60:
#     print('合格!')
#     print('よく頑張りましたね!')
# else:
#     print('残念ながら不合格です')
#     print('追記試験を受けてください')

# if文のネスト

print('すべての質問に y または n で答えてください')
okane_aruka = input('お金に余裕はありますか? >>')
if okane_aruka == 'y':
    onaka_suiteruka = input('お腹がすごく空いていますか? >>')
    nomitai_kibunka = input('ビール飲みたいですか? >>')
    if onaka_suiteruka == 'y' and nomitai_kibunka == 'y':
        print('焼肉はいかがですか')
    elif onaka_suiteruka == 'y':
        print('カレーはいかがですか')
    elif nomitai_kibunka == 'y':
        print('焼き鳥はいかがですか')
    else:
        print('パスタはいかがですか')
        yashoku_iruka = input('夜食は必要ですか? >>')
        if yashoku_iruka == 'y':
            print('コンビニのチキンはいかがですか')
        else:
            print('家で食べましょう')
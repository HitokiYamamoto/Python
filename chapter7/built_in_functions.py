# text = input('何を記録しますか? >>')
# file = open('chapter7/diary.txt', 'a')
# file.write(text + '\n')
# file.close()


# 用が済んだらすぐにファイルを閉じる
text = input('今日は何をした? >>')
with open('chapter7/diary2.txt', 'a') as file:
    file.write(text + '\n')
# 身長(cm)の入力
height_cm = float(input("身長(cm)を入力してください: "))

# 体重(kg)の入力
weight_kg = float(input("体重(kg)を入力してください: "))

# 身長をメートルに変換
height_m = height_cm / 100

# BMIの計算
bmi = weight_kg / (height_m * height_m)

# 結果の表示
print("BMIは {:.2f} です。".format(bmi))

# BMIの分類
if bmi < 18.5:
    print("低体重")
elif 18.5 <= bmi < 25:
    print("正常体重")
elif 25 <= bmi < 30:
    print("肥満（1度）")
elif 30 <= bmi < 35:
    print("肥満（2度）")
elif 35 <= bmi < 40:
    print("肥満（3度）")
else:
    print("肥満（4度）")

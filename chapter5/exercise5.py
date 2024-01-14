# 西暦を渡すと、閏年かを判定させるis_leap_year関数を作成

# def is_leap_year(year):
#     if year % 4 == 0 and (year % 400 == 0 or 
#                           year % 100 != 0):
#         print(f'西暦{year}年は、閏年です')
#     else:
#         print(f'西暦{year}年は、閏年ではありません')

# year = int(input('西暦を入力してください >>'))
# is_leap_year(year)


# 割り勘計算プログラム
def dutch_treat():
    def int_input():
        amount = int(input('支払い総額を入力してください >>'))
        people = int(input('参加人数を入力してください >>'))
        print(f'支払総額額{amount}円')
        print(f'参加人数{people}人')
        return amount, people
    amount, people = int_input()

    def calc_payment(amount, people):
        d_num = amount / people
        pay = d_num // 100 * 100
        if d_num > pay:
            pay = int(pay + 100)
        pay_log = amount - pay * (people - 1)
        print(f'1人あたり{pay}円、幹事は{pay_log}円の支払い')
        return pay, pay_log
    pay, pay_log = calc_payment(amount, people)

    def show_payment(pay, pay_log, people,):
        print('***支払額***')
        print(f'1人あたり{pay}円({people}人)、幹事は{pay_log}円です')
    show_payment(pay, pay_log, people)

dutch_treat()
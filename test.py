# 順次進行

print("Good morning")

print("good afternoon")

print("good evening")

# 変数

num = 1
num01 = 2
num_01 = 3

print(num)
print(num01)
print(num_01)

# データ型

num01 = 123
num02 = 1.23

print(type(num01))
print(type(num02))

string_a = "Hello, world!"

print(string_a)
print(type(string_a))

a = 10
b = 1

bool01 = (a > b)
# bool01 = (a < b)

print(bool01)
print(type(bool01))

# リスト

a = [["yamamoto", "suzuki"],[ "tanaka", "takahashi"]]

print(a[0][0])
print(a[0][1])
print(a[1][0])
print(a[1][1])

# 演算子

x = 10
y = 2
z = 10

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

# 関係演算子

print(x < y)
print(x > y)
print(x <= y)
print(x >= z)
print(x == y)
print(x != y)

# 論理演算子

print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)
print(x == 10 or y == 1)
print(x == 1 or y == 1)

# 代入演算子

x += 10
z += y

print(x)
print(z)

# 条件分岐

age = 0

if age >= 20:
  print("adult")
elif age == 0:
  print("baby")
else:
  print("child")

# 繰り返し

for i in range(5):
  print(i)

for i in range(5):
  if i == 3:
    break
  print(i)

  for i in range(5):
    if i == 3:
      continue
    print(i) 

  for i in range(3):
    for j in range(3):
      print(i, j ,sep="-")

  arr = [2, 4, 6, 8, 10]
  sum = 0
  for i in arr:
    sum += i
  print(sum)

  #　関数

def say_hello(greeting):
  print(greeting)
say_hello("hello world")
say_hello("good morning")
say_hello("good evening")

def add(num1, num2):
  return(num1 + num2)
add_result = (add(6, 2))
print(add_result)

# 3つの引数を受け取る関数を作り、9と4と2の平均を出す

def average (num1, num2, num3):
  return(num1 + num2 + num3) / 3
average_result = average(9, 4, 2)
print(average_result)

# アトリビュート/メソッド

class Student:  # 先頭大文字が慣習

  def __init__(self, name):
    self.name = name

  def avg(self, math, english):    # 渡したい引数が無くても引数が必要。その場合"self"と書くのが慣習
    print((math + english) / 2)

a001 = Student("sato")
a001.avg(80, 70)
print(a001.name)

a002 = Student("yamamoto")
a001.avg(60, 80)
print(a002.name)

# 実践

class Student:
  
  def __init__(self, name):
    self.name = name

  def calculate_avg(self, date):
    sum = 0

    for num in date:
      sum += num
    
    avg = sum / len(date)
    return avg
  
  def judge(self, avg):

    if(avg >= 60):
      result = "passed"
    else:
      result = "failed"
    return result
  
  a001 = Student("sato")
  date = [70, 65, 50, 90, 30]
  avg = a001.calculate_avg(date)
  result = a001.judge(avg)

  print(avg)
  print(a001.name + "" + result)

  
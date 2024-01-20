# mathモジュールを利用する

# import math

# print(f'円周率は{math.pi}です')
# print(f'小数点以下を切り捨てれば{math.floor(math.pi)}です')
# print(f'小数点以下を切り上げれば{math.ceil(math.pi)}です')

# 特定の変数や関数だけを利用する

from math import floor
from math import pi

print(f'円周率は{pi}')
print(f'小数点以下を切り捨てれば{floor(pi)}です')
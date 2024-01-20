# %matplotlib inline
# import matplotlib.pyplot as plt 

# weight = [68.4, 68.0, 69.5, 68.4, 68.6, 70.2, 71.4, 70.8,
#           68.5, 68.6, 68.3, 68.4]
# plt.plot(weight)
# plt.show()

# requestsでPythonの公式サイトを取得する

import requests

response = requests.get('https://www.python.org/downloads/')
text = response.text
print(text)
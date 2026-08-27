# contagem regressiva começando do 5
import time
n = int(input('Digite Quanto você quer de contagem regressiva: '))

for i in range(5,-n,-1):
    if i < 1:
        break
    time.sleep(1)
    print(i)
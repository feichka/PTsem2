#Монету подбросили 144 раза.
# Какова вероятность, что орел выпадет ровно 70 раз?
import math

n = 144
k = 70
p = 0.5
q = 1-p
#c = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
c = math.comb(n,k)
x = (c*(p**k)*(q**(n-k)))
print(f"Вероятность, что орел выпадет 70 раз равна {x}, или {round(x*100,2)} %")

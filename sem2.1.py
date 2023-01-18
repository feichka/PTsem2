# Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8.
# Стрелок выстрелил 100 раз. Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.

import math

p = 0.8
n = 100
k = 85
q = 1-p
c = math.comb(n, k)
x = c*(p**k)*(q**(n-k))
print(f"Вероятность попасть 85 раз из 100 составляет {x}, или {round (x*100,2)} %")

import re

S = "jjhv"
k = "z"
increment = 0

m = re.search(k, S)
if not m:
    print((-1, -1))
while m:
    start = m.start()
    end = m.end()
    print((m.start() + increment, m.end() - 1 + increment))
    S = S[m.start()+1:]
    increment += m.start()+1
    m = re.search(k, S)

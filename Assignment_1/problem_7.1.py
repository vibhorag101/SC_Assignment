from math import log
ans = 0
for i in range(1, 5001):
    term1 = 0
    for j in range(1, i+1):
        term1 += 1/j
    lnI = log(i)
    ans = term1 - lnI
    if(i % 100 == 0):
        print("current n is", i, "and the value of term is", ans)
print("The final estimated value of eulers constant is", ans)

# current n is 4100 and the value of term is 0.5773376111636459
# current n is 4200 and the value of term is 0.5773347077964406
# current n is 4300 and the value of term is 0.577331939464333
# current n is 4400 and the value of term is 0.5773292969607322
# current n is 4500 and the value of term is 0.5773267718973916
# current n is 4600 and the value of term is 0.5773243566154296
# current n is 4700 and the value of term is 0.5773220441077846
# current n is 4800 and the value of term is 0.5773198279512748
# current n is 4900 and the value of term is 0.5773177022470506
# current n is 5000 and the value of term is 0.577315661568166
# The final estimated value of eulers constant is 0.577315661568166

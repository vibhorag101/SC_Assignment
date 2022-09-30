from math import log
ans = 0
for i in range(1, 5001):
    term1 = 0
    for j in range(1, i+1):
        term1 += 1/j
    lnI = log(i+(1/2))
    ans = term1 - lnI
    if(i % 100 == 0):
        print("current n is", i, "and the value of term is", ans)
print("The final estimated value of eulers constant is", ans)

# current n is 4100 and the value of term is 0.5772156673795781
# current n is 4200 and the value of term is 0.5772156672629993
# current n is 4300 and the value of term is 0.5772156671544533
# current n is 4400 and the value of term is 0.5772156670532187
# current n is 4500 and the value of term is 0.5772156669586632
# current n is 4600 and the value of term is 0.5772156668702006
# current n is 4700 and the value of term is 0.5772156667873283
# current n is 4800 and the value of term is 0.5772156667095789
# current n is 4900 and the value of term is 0.5772156666365351
# current n is 5000 and the value of term is 0.5772156665678327
# The final estimated value of eulers constant is 0.5772156665678327

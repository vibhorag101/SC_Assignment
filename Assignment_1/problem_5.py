import numpy as np
from decimal import Decimal

pi = np.pi
inputArg = []
for i in range(0, 21):
    inputArg.append((pi/4) + 2*pi*(10**(i)))

tanOut = np.tan(inputArg)
sinOut = np.sin(inputArg)
cosOut = np.cos(inputArg)
conditionNumber = []
relativeForwardError = []
relativeBackwardError = []
inputError = []
for i in range(0, 21):
    conditionNumber.append(abs(Decimal(inputArg[i])/Decimal((sinOut[i]*cosOut[i]))))
    relativeForwardError.append(abs(Decimal(tanOut[i]-1)))
    relativeBackwardError.append(Decimal(relativeForwardError[i])/Decimal(conditionNumber[i]))
    inputError.append(Decimal(inputArg[i])*Decimal(relativeBackwardError[i]))



for i in range(0, 21):

    print("The value of j is", i)
    print("(x,tan(x) = (%1.16f,%1.16f)" % (inputArg[i], tanOut[i]))
    print("Condition number is %1.16f" % (conditionNumber[i]))
    print("Relative backward error is", relativeBackwardError[i])
    print("Error in the input is", inputError[i])

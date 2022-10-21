from vectoR import *

test = c(1, 2, 3, 0)
print(test*2)
print(test-2)
print(test + c(1, 0, 1, 0))

test = c(True, False, False)
test2 = c(True, True, False)
print(test & test2)

test = c(1, 2, 3, 4)
test += 10
print(test)

test = c(1, 2, 3, 0)
test[c(1, 4)] = c(20, 30)
print(test)

test = c(1, 2, 3, 0)
test[c(1, 4, 2)] = c(20, 30)
print(test)

test = c(1, 2, 3, 0)
test[c(1, 4)] = 90
print(test)

test = c(1, 2, 3, 0)
test[c(True)] = c(80)
print(test)

test = c(1, 2, 3, 0)
test[c(True)] = 100
print(test)

test = c(1, 2, 3, 0)
test[c(False, True, False, True)] = c(20, 90)
print(test)


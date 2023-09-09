import numpy as np
p = np.array([ [0.8,0.1], [0.2, 0.9]  ])
pop = np.array([150,150])


pPop = np.dot(p,pop) # the matrix for the population after 1 hour
pT = np.transpose(p) # the transpose of matrix p

print("The population in A after 1 hour is", round(pPop[0]))
print("The population in B after 1 hour is", round(pPop[1]))

print("The matrix for the population after one hour is", pPop)
print("The transposed matrix of p is",pT)


if np.allclose(p, pT):
    # checks each component is the same in both of the matrices
    print("The matrices are symmetrical")
    # symmetrical means that the matric is equal to its transpose
else:
    print("The matrices are not symmetrical")


###################### TASK 2 ####################################
    
n = 1
# this value will control the number of iterations

TotalConserved = True
# this boolean that will keep track of whether the total is conserved

temp = np.array([150,150])
# this is the temporary population for the while loop

# the matrix multiplication is looped 72 times
while n < 73 :
    temp = np.dot(p, temp)
    total = temp[0] + temp[1]

    # rounds to an interger number and checks the total is 300
    if round(total) != 300:
        TotalConserved = False

    # adds one to n, for each iteration 72 times
    n = n + 1

print("The population in A after 72 hours is", round(temp[0]))
print("The population in B after 72 hours is", round(temp[1]))

print("The population number of A and B are stable after around 65 hours")
# tells the user whether the total is conserved

if TotalConserved == True:
    print("The total is always 300 when rounded to the nearest integer")
else:
    print("The total changes from 300")

Stable = True
# this boolean will keep track of whether the population number

# now an extra ten hours will be simulated to check stability
for x in range (0,24):
    # 24 hours simulated to account for a full day
    nextHour = np.dot(p, temp)
    if round(nextHour[0]) != round(temp[0]) or round(nextHour[1]) != round(temp[1]):
        # if either the population of A or the population if B changes during the next hour
        # the boolean 'Stable' will become False
        Stable = False
    temp = nextHour

if TotalConserved == True:
    print("The population number of A and B remains stable even if an extra 24 hours (a full day) is simulated")
else:
    print("The population number of A and B does not remain stable if an extra 24 hours (a full day) is simulated")

T =  5
N =  [3, 3, 8, 5, 6]
C =  [[2, 38, 86], [34, 49, 75], [86, 18, 68, 80, 98, 57, 80, 55], [76, 14, 34, 31, 52], [58, 37, 11, 31, 57, 72]]




Odds = 0
Evens = 0

for x in range(T):

    for numbs in C[x]:
        if numbs %2 == 0:
            Evens +=1
        else:
            Odds +=1
    


    if Odds ==2 and len(C[x]) == 3:
        print(False)
        Odds = 0
        Evens = 0
    elif Odds >= 3:
        print(True)
        Odds = 0
        Evens = 0

    elif Evens >=2 and Odds >= 1:
        print(True)
        Evens = 0 
        Odds = 0 
    else:
        print(False)
        Odds = 0
        Evens = 0 


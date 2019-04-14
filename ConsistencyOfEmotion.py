def ConsistencyOfEmotion(outcome,n,layer):
    resultOdourEmotion=[[0 for col in range(3)] for row in range(14)]
    resultColourEmotion=[[0 for col in range(3)] for row in range(n)]
    i=0

    while i<(n*layer):
        if (i%n)==14:
            i+=22
            if i==(n*layer):
                break

        if outcome[i][6]==str(1):
            resultOdourEmotion[i%n][1]+=1
        elif outcome[i][6]==str(0):
            resultOdourEmotion[i%n][0]+=1
        else :
            resultOdourEmotion[i%n][2]+=1
        i+=1
    for i in range(14):
        print(resultOdourEmotion[i])


    print('')
    i=0
    while i<(n*layer):
        if i==(n*layer):
            break
        else:
            if outcome[i][7]==str(1):
                resultColourEmotion[i%n][1]+=1
            elif outcome[i][7]==str(0):
                resultColourEmotion[i%n][0]+=1
            else:
                resultColourEmotion[i%n][2]+=1
        i+=1

    for i in range(n):
        print(resultColourEmotion[i])

    return resultOdourEmotion, resultColourEmotion
layer=31
n=36 # 첫행은 이름

outcome= [0 for row in range(n*layer)]

for i in range(n*layer):
    outcome[i]=input()
    outcome[i]=outcome[i].split('\t')

result1=[[0 for col in range(3)] for row in range(14)]
result2=[[0 for col in range(3)] for row in range(n)]
result1, result2=ConsistencyOfEmotion(outcome,n,layer)

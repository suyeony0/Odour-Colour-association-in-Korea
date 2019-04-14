'''어울리거나 어울리지않는 색깔 총합하는 프로그램 + 색깔 계열별로 총합하는 프로그램'''
def congruent1(outcome,n,layer):
    result=[[0 for col in range(37)] for row in range(15)]
    for i in range(n*layer):
            result[i%(n)][int(outcome[i][0])]+=1
    for i in range(n):
        print(result[i])
    return result
def congruent2(outcome,n,layer):
    result=[[0 for col in range(37)] for row in range(15)]
    for i in range(n*layer):
        for j in range(3):
            result[i%(n)][int(outcome[i][j])]+=1
    for i in range(n):
        print(result[i])
    return result
def uncongruent(outcome,n,layer):
    result=[[0 for col in range(37)] for row in range(15)]
    for i in range(n*layer):
        for j in range(3,6):
            result[i%(n)][int(outcome[i][j])]+=1
    for i in range(n):
        print(result[i])
    return result


def combineSimilarColours(outcome,n,layer):
    temp=0
    result=[[0 for col in range(10)] for row in range(n)]
    for i in range(n*layer):
        for j in range(3):
            if outcome[i][j]==str(12) or outcome[i][j]==str(30) or outcome[i][j]==str(33) or outcome[i][j]==str(35) :
                result[i%n][1]+=1
            elif outcome[i][j]==str(2) or outcome[i][j]==str(10) or outcome[i][j]==str(14) or outcome[i][j]==str(19) :
                result[i%n][2]+=1
            elif outcome[i][j]==str(4) or outcome[i][j]==str(5) or outcome[i][j]==str(24) or outcome[i][j]==str(29) :
                result[i%n][3]+=1
            elif outcome[i][j]==str(7) or outcome[i][j]==str(11) or outcome[i][j]==str(13) or outcome[i][j]==str(31) :
                result[i%n][4]+=1
            elif outcome[i][j]==str(3) or outcome[i][j]==str(15) or outcome[i][j]==str(17) or outcome[i][j]==str(28) :
                result[i%n][5]+=1
            elif outcome[i][j]==str(6) or outcome[i][j]==str(16) or outcome[i][j]==str(20) or outcome[i][j]==str(27) :
                result[i%n][6]+=1
            elif outcome[i][j]==str(1) or outcome[i][j]==str(8) or outcome[i][j]==str(22) or outcome[i][j]==str(25) :
                result[i%n][7]+=1
            elif outcome[i][j]==str(18) or outcome[i][j]==str(32) or outcome[i][j]==str(34) or outcome[i][j]==str(36) :
                result[i%n][8]+=1
            elif outcome[i][j]==str(9) or outcome[i][j]==str(21) or outcome[i][j]==str(23) or outcome[i][j]==str(26) :
                result[i%n][9]+=1
            else : #0의 개수
                result[i%n][0]+=1
    for i in range(n):
        print(result[i])
    return result

def uncombineSimilarColours(outcome,n,layer):
    temp=0
    result=[[0 for col in range(10)] for row in range(n)]
    for i in range(n*layer):
        for j in range(3,6):
            if outcome[i][j]==str(12) or outcome[i][j]==str(30) or outcome[i][j]==str(33) or outcome[i][j]==str(35) :
                result[i%n][1]+=1
            elif outcome[i][j]==str(2) or outcome[i][j]==str(10) or outcome[i][j]==str(14) or outcome[i][j]==str(19) :
                result[i%n][2]+=1
            elif outcome[i][j]==str(4) or outcome[i][j]==str(5) or outcome[i][j]==str(24) or outcome[i][j]==str(29) :
                result[i%n][3]+=1
            elif outcome[i][j]==str(7) or outcome[i][j]==str(11) or outcome[i][j]==str(13) or outcome[i][j]==str(31) :
                result[i%n][4]+=1
            elif outcome[i][j]==str(3) or outcome[i][j]==str(15) or outcome[i][j]==str(17) or outcome[i][j]==str(28) :
                result[i%n][5]+=1
            elif outcome[i][j]==str(6) or outcome[i][j]==str(16) or outcome[i][j]==str(20) or outcome[i][j]==str(27) :
                result[i%n][6]+=1
            elif outcome[i][j]==str(1) or outcome[i][j]==str(8) or outcome[i][j]==str(22) or outcome[i][j]==str(25) :
                result[i%n][7]+=1
            elif outcome[i][j]==str(18) or outcome[i][j]==str(32) or outcome[i][j]==str(34) or outcome[i][j]==str(36) :
                result[i%n][8]+=1
            elif outcome[i][j]==str(9) or outcome[i][j]==str(21) or outcome[i][j]==str(23) or outcome[i][j]==str(26) :
                result[i%n][9]+=1
            else : #0의 개수
                result[i%n][0]+=1
    for i in range(n):
        print(result[i])
    return result

def firstCombineSimilarColours(outcome,n,layer):
    result=[[0 for col in range(10)] for row in range(15)]
    for i in range(n*layer):
        j=0
        if outcome[i][j]==str(12) or outcome[i][j]==str(30) or outcome[i][j]==str(33) or outcome[i][j]==str(35) :
            result[i%n][1]+=1
        elif outcome[i][j]==str(2) or outcome[i][j]==str(10) or outcome[i][j]==str(14) or outcome[i][j]==str(19) :
            result[i%n][2]+=1
        elif outcome[i][j]==str(4) or outcome[i][j]==str(5) or outcome[i][j]==str(24) or outcome[i][j]==str(29) :
            result[i%n][3]+=1
        elif outcome[i][j]==str(7) or outcome[i][j]==str(11) or outcome[i][j]==str(13) or outcome[i][j]==str(31) :
            result[i%n][4]+=1
        elif outcome[i][j]==str(3) or outcome[i][j]==str(15) or outcome[i][j]==str(17) or outcome[i][j]==str(28) :
            result[i%n][5]+=1
        elif outcome[i][j]==str(6) or outcome[i][j]==str(16) or outcome[i][j]==str(20) or outcome[i][j]==str(27) :
            result[i%n][6]+=1
        elif outcome[i][j]==str(1) or outcome[i][j]==str(8) or outcome[i][j]==str(22) or outcome[i][j]==str(25) :
            result[i%n][7]+=1
        elif outcome[i][j]==str(18) or outcome[i][j]==str(32) or outcome[i][j]==str(34) or outcome[i][j]==str(36) :
            result[i%n][8]+=1
        elif outcome[i][j]==str(9) or outcome[i][j]==str(21) or outcome[i][j]==str(23) or outcome[i][j]==str(26) :
            result[i%n][9]+=1
        else : #0의 개수
            result[i%n][0]+=1
    for i in range(n):
        print(result[i])
    return result


layer=31
n=14
outcome=[0 for i in range(n*layer)]
for i in range(n*layer):
    outcome[i]=input()
    outcome[i]=outcome[i].split('\t')


print("Congruent")
congruent1(outcome,n,layer)
print("Multi-Congruent")
congruent2(outcome,n,layer)
print("Multi-Unongruent")
uncongruent(outcome,n,layer)
print("first-CongruentColours")
firstCombineSimilarColours(outcome,n,layer)
print("Mulit-combineColours")
combineSimilarColours(outcome,n,layer)
print("Multi-uncombineColours")
uncombineSimilarColours(outcome,n,layer)

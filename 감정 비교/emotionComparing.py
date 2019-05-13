'''
각 냄새마다 냄새에 대한 감정과 색깔에 대한 감정의 일치개수를 계산하는 프로그램
즉, 양상간 일치성
'''
def emotionComparing(outcome,n,layer):
    result=[0 for row in range(14)]

    i=0
    while i<(n*layer):

        if (i%n)==14:
            i+=22
            if i==(n*layer):
                break

        for j in range(3):
        #for j in range(1):
            if outcome[i][j]==str(0):
                #if outcome[i][6]==outcome[int(outcome[i][0])-1][7]: # 냄새에 대한 색깔을 3개다 고르지 않았을 경우 첫번째 것을 반복적으로 사용할 경우
                    #result[i%n]+=0.33
                result[i%n]+=0.33 # 색깔을 고르지 않은 경우 1/3 분의 확률로 일치하므로 0.33 의 값을 부여
            elif outcome[i][6]==outcome[int(outcome[i][j])-1][7]: #냄새에 대한 감정과 색깔에 대한 감정을 비교하여 감정이 일치하면 1을 더함
                result[i%n]+=1

        i+=1
    for l in range(14):
        print(result[l])
    return result

layer=31
n=36 # 첫행은 이름

outcome= [0 for row in range(n*layer)]

for i in range(n*layer):
    outcome[i]=input()
    outcome[i]=outcome[i].split('\t')


result=emotionComparing(outcome,n,layer)
sum=0
for i in range(14):
    sum+=result[i]
print(sum/14)

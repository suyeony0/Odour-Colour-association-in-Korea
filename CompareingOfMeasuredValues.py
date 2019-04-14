'''냄새의 신체 변화와 색깔의 신체 변화의 일치성 분석'''
layer=31
n=14
m=36
temp= n*layer
temp2= m*layer
outcome= [0 for row in range(temp)]
odourHeartbit=[0 for row in range(temp)]
odourMyogram=[0 for row in range(temp)]
colourHeartbit=[0 for row in range(temp2)]
colourMyogram=[0 for row in range(temp2)]
resultHeartbit=[0 for row in range(temp)]
resultMyogram=[0 for row in range(temp)]
totalRatio=0
#인풋 받기 1. 색깔 2. 냄새 심박수 3. 냄새 근전도 4. 색깔 심박수 5. 색깔 심박수

for i in range(temp): #format input의 연관된, 연관되지 않은 색깔들을 outcome 배열에 리스트화 시킴
    outcome[i]=input()
    outcome[i]=outcome[i].split('\t')

for i in range(temp):
    odourHeartbit[i]=input()

for i in range(temp):
    odourMyogram[i]=input()

for i in range(temp2):
    colourHeartbit[i]=input()

for i in range(temp2):
    colourMyogram[i]=input()


#각 냄새의 심박수, 근전도를 7/6 을 곱한것과 그 냄새의 색깔 3개의 심전도, 금전도를 더하것을 비교
for i in range(temp):
    a=int(outcome[i][0])
    b=int(outcome[i][1])
    c=int(outcome[i][2])
    if odourHeartbit[i]==str(0):
        resultHeartbit[i]=0
    else:
        #색깔을 3개다 고르지 않았을 경우 고르지 않은 색깔에 대한 일치할 확률을 1/3으로 가정
        if c==0:
            if b==0:
                resultHeartbit[i]=(float(odourHeartbit[i])*(7/6))/(float(colourHeartbit[a-1])+(2/3))
                continue
            else :
                resultHeartbit[i]=(float(odourHeartbit[i])*(7/6))/((float(colourHeartbit[a-1])+float(colourHeartbit[b-1])+(1/3)))
                continue
        else:
            resultHeartbit[i]=(float(odourHeartbit[i])*(7/6))/(float(colourHeartbit[a-1])+float(colourHeartbit[b-1])+float(colourHeartbit[c-1]))

for i in range(temp):
    a=int(outcome[i][0])
    b=int(outcome[i][1])
    c=int(outcome[i][2])
    if odourMyogram[i] == str(0) :
        resultMyogram[i]=0
    else:
        #색깔을 3개다 고르지 않았을 경우 고르지 않은 색깔에 대한 일치할 확률을 1/3으로 가정
        if c==0:
            if b==0:

                resultMyogram[i]=(float(odourMyogram[i])*(7/6))/(float(colourMyogram[a-1])+(2/3))
                continue
            else :
                resultMyogram[i]=(float(odourMyogram[i])*(7/6))/((float(colourMyogram[a-1])+float(colourMyogram[b-1])+(1/3)))
                continue
        else:
            resultMyogram[i]=(float(odourMyogram[i])*(7/6))/((float(colourMyogram[a-1])+float(colourMyogram[b-1])+float(colourMyogram[c-1])))




count=0
average=0 #심박수 평균
average2=0 #근전도 평균
for i in range(temp):
    #몇번째 실험자인지 표기하기 위한 if문
    if i%n ==0 :
        count+=1
        print('')
        #print(count,"번째 실험자")
#냄새 심박,근전도 나누기 색깔 심박 근전도의 결과
    if resultMyogram[i]==0 :
        average+=resultHeartbit[i]
        print(resultHeartbit[i],",",0)

    elif resultHeartbit[i]==0:
        average2+=resultMyogram[i]
        print(0,",",resultMyogram[i])

    else:
        average+=resultHeartbit[i]
        average2+=resultMyogram[i]
        print(resultHeartbit[i],",",resultMyogram[i])

    if i>1 and (count*n-1)/i ==1 and resultMyogram[i]==0:
        print(average) #심박수 총합
        print(average/n)# 심박수 평균
        totalRatio+=average
        average=0
    elif i>1 and (count*n-1)/i ==1 and resultHeartbit[i]==0:
        print(',',average2)#근전도 총합
        print(',',average2/n)#근전도 평균
        totalRatio+=average2
        average2=0
    elif i>1 and (count*n-1)/i ==1:
        print(average,',',average2)#심박수 총합과 근전도 총합
        print(average/n,',',average2/n)
        print((average+average2)/(n*2))# 심박수 + 근전도 의 평균
        totalRatio+=(average+average2)/2
        #근전도, 심박 두개의 센서가 모두 측정 된것은 두개의 총 값을 더해 2로 나누어 평균을만들어
        #1명분으로 totalRatio에 더해준다.
        average=0
        average2=0

print(totalRatio/layer)


print('')
'''
count=0
average=0
for i in range(temp):
    if  i%n == 0 :
        count+=1
        print('')
        print(count,"번째 실험자")


    average+=resultMyogram[i]
    print(resultMyogram[i])
    if i>1 and (count*n-1)/i ==1:
        print("합계 : ",average)
        print("평균 : ", average/n)
        average=0'''

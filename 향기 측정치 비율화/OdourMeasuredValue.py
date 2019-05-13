def ratioOfHeartBit(heartBit,n,layer):
    '''각 실험자마다 14개의 각 냄새에 대한 심박수 비율을 계산해주는 프로그램'''
    result = [[0 for col in range(n)] for row in range(layer)]
    l=0

    for i in range(layer):

        sum=0
        currentSum=0
        if heartBit[i*n]!='':
            for k in range(i*n,(i+1)*n):
                currentSum+=int(heartBit[k])

        for j in range(n):
            '''근전도 데이터가 없을 경우 빈 칸으로 채운다'''
            if heartBit[i*n]=='':
                result[i][j]=0
                l+=1
                print(result[i][j])
                continue
            result[i][j]=int(heartBit[l])/currentSum
            print(result[i][j])
            sum+=result[i][j]
            l+=1


    return result

def ratioOfMyogram(myogram,n,layer):
    '''각 실험자마다 14개의 각 냄새에 대한 근전도 비율을 계산해주는 프로그램'''
    result = [[0 for col in range(n)] for row in range(layer)]
    l=0

    for i in range(layer):

        sum=0
        currentSum=0
        if myogram[i*n]!='':
            for k in range(i*n,(i+1)*n):
                currentSum+=int(myogram[k])

        for j in range(n):
            '''근전도 데이터가 없을 경우 빈 칸으로 채운다'''
            if myogram[i*n]=='':
                result[i][j]=0
                l+=1
                print(result[i][j])
                continue
            result[i][j]=int(myogram[l])/currentSum
            print(result[i][j])
            sum+=result[i][j]
            l+=1

    return result






n=14
layer=31

heartBit=[0 for i in range(n*layer)]
myogram=[0 for i in range(n*layer)]
outcome=[0 for i in range(n*layer)]

for i in range(n*layer):
    outcome[i]=input()
    outcome[i]=outcome[i].split('\t')
    heartBit[i]=outcome[i][0]
    myogram[i]=outcome[i][1]

#print('heartBit')
ratioOfHeartBit(heartBit,n,layer)
#print('Myogram')
ratioOfMyogram(myogram,n,layer)

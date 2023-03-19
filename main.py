# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    #izveidoju masīvu, kurā glabāšu threads
    threads=[]
    #tik cik n jeb cik thredi nepieciešami
    for i in range (n):
        threads.append(0)
    #data salieku listā, iegūstu tā garumu, kuru izmantošu, lai noskaidrotu, cik mainīgie listā vēl palikuši
    data = list(map(int, data.split()))
    #izveidoju mainīgo laiks, lai zinātu, cik ilgs laiks jau pagājis
    time=0
    while True :
        for i in range(n):
            #ja threads[n]ir tukšs es tam piešķiru vērtību, laiks plus data[i], lai zinātu, kad nākamais mainīgais jāievieto šajā vietā.
            if threads[i]==time:
                output.append([i, time])
                #print("threads[i]=",threads[i])
                #print("data[0]=",data[0])
                threads[i]=time+data[0]
                data.pop(0) 
                if len(data)==0: 
                    return output

        time=time+1
        
    

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    firstLine=input()
    splitedFL=firstLine.split()
    n = int(splitedFL[0])
    m = int(splitedFL[1])
    dataLine=input()
    dataLine.split()
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = dataLine
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in result:
        for j in i:
            print(j, end=" ")
        print()
    


if __name__ == "__main__":
    main()

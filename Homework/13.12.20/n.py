def gameList():
    coin1to2=0
    nlydzew = int(input("Введите число n людей : "))
    mlydzew = int(input("Введите число m людей : "))
    lydList = []
    mList = []
    coin1to2 = 0
    coinList = []

    for i in range(1, nlydzew + 1):
        coinList += '0'
    for i in range(1, nlydzew + 1):
        lydList += str(i)
    for i in range(1, mlydzew + 1):
        mList += str(i)



    for i in range(len(coinList) - 1):
        for j in range(1,len(coinList) - 1):


            if i==mList[-1] :

                for k1 in range( len(mList) - 1):
                    if mList<lydList:
                        for coin in range(1,len(mList)-1):
                            coinList[coin]+=1
                        for coin3 in range(len(lydList)):
                            if coin3>len(mList) :
                                coinList [coin3] += 2
                    elif mList>=lydList:
                        for coin1 in range(len(lydList)-1):
                            coinList[coin1]+=1
                coin1to2=coinList[i]
                coinList[i+1] += coin1to2
                coinList.remove(coinList[i])
                lydList.remove(lydList[i])
    print(lydList,"\n",coinList)





gameList()
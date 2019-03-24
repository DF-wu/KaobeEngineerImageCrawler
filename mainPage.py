import PythonCrawlerForKaobeiEngineer as ps


def main(): 
    categoryStr = ['','monthly','quarterly','top2018']
                # weektop , monthluTop, seasonTop, yearTop
    
    messageStr  = ['1.周排名','2.月排名','3.季排名','4.2018排名']
    
    print("欲爬下來的圖片分類 請輸入數字")
    for i in range(4):
        print(messageStr[i])
    selection =  input()
    intSelection = int(selection)

    while intSelection >=1 and intSelection <= 4:
        selection =  input()
        intSelection = int(selection)
        ps.htmlPaserAndDownloader(categoryStr[ intSelection ],categoryStr[intSelection]+"top")
    else:
        print("輸入錯誤，請重新輸入")
        print("欲爬下來的圖片分類 請輸入數字")
        for i in range(4):
            print(messageStr[i])


print('done')

if __name__ == '__main__':
    main()  # 或是任何你想執行的函式
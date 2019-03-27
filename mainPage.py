import PythonCrawlerForKaobeiEngineer as ps

def main(): 
    categoryStr = ['','monthly','quarterly','top2018']
                # weektop , monthluTop, seasonTop, yearTop
                #  
    messageStr  = ['1.周排名','2.月排名','3.季排名','4.2018排名']
    
    print("欲爬下來的圖片分類 請輸入數字")

    for i in range(4):
        print(messageStr[i])

    selection =  int(input()) - 1
    while (selection > 3) or (selection < 0):
        #輸入錯誤部分
        # 輸入跟index是不同的
        
        print("輸入錯誤，請重新輸入")
        for i in range(4):
            print(messageStr[i])
        selection =  int(input()) -1
    else:
        ps.htmlPaserAndDownloader(categoryStr[ selection ], messageStr[selection])
        print("call func")


print('done')



if __name__ == '__main__':
    main()  # 或是任何你想執行的函式
    print('execute localy module')
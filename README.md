# 功能  
* 計算GAP(測站最大空餘角)  
* 計算測站觸發用時*  
  *僅使用編號時有效
# 使用方法  
### 執行程式
  下載後執行`start.bat`  
### 設定金鑰
  初次啟動時程式會詢問是否有金鑰，有則輸入，無則直接按下Enter即可  
  金鑰存放在`key.txt`內，若金鑰有需更改請直接修改檔案內容  
### 開始計算
  1. 選擇資料輸入方式，檢知編號(推薦)`1`、測站代碼`2`、測站座標`3`
  2. 資料輸入  
      * 檢知編號  
        1. 輸入檢知編號  
           若取得地震資料失敗，需手動輸入震央座標  
      * 測站代碼、座標
        1. 輸入震央座標
        2. 輸入測站數量
        3. 輸入測站編號或經度、緯度  
           測站編號包含「-」符號，若輸入錯誤測站編號時，會要求手動輸入經緯度
### 計算結果
  * GAP  
    * 3站以上輸出最大角度  
    * 2站輸出最大角度及最小角度  
    * 輸出到小數點後2位  
  * 測站觸發耗時  
    * 僅在使用檢知編號時顯示
    * 若未取得震央資訊時不顯示
# 備註  
* 需安裝`Python`環境 ([下載連結](https://www.python.org/downloads/))
* 需安裝`Python`模組**  
  **若執行時出現`ModuleNotFoundError: No module named 'urllib3'`或`ModuleNotFoundError: No module named 'requests'`
    
  安裝方式: 在終端機/命令提示字元內輸入下方指令(僅需安裝缺少的部分)  
  `pip install urllib3`  
  `pip install requests`  
* 金鑰用於取得TYA地震報告的震央資訊

# 計算理論 1101 期末專題 
> 姓名：余紹桓  
> 學號：F74084737  
> 系級：資訊系112甲  
# 好傑寶LineBot 
![抽抽樂](https://user-images.githubusercontent.com/46813276/147873176-7e69d8e9-bacf-4ace-ad5e-d548c0cce20e.png)
![RogerHi](https://user-images.githubusercontent.com/46813276/147873179-580e53ec-9483-4b1a-b402-ff1beabb8431.png)

## 資訊  
機器人ID : @841irdwl  
![image](https://user-images.githubusercontent.com/46813276/147873204-e42354f0-e239-4302-9947-4effb46a92bc.png)
## 介紹
好傑寶LineBot可以幫你**抓取羅傑YT頻道的最新影片**，隨機抽取**羅傑梗圖**等等，  
另外好傑寶LineBot使用了**Google試算表**來當作**梗圖資料庫** (大家共用)  
能讓使用者在LineBot中新增、移除資料庫裡的梗圖， (資料庫操作)    
當然也可以直接去那張Google試算表更改。  

LineBOT也提供了紀錄YT最愛影片的功能，也會新增到相同的試算表中 (大家共用)   
不過因為這個機器人只有我在用，所以資料庫共用應該沒問題吧...  

而在新增最愛影片網址與新增Imgur圖片網址的動作中，  
好傑寶會使用**正規表達式**來幫您檢查**該網址是否有符合規定**，  
如果不符，好傑寶就不會幫你把資料加進去試算表囉！  

## 使用過程

* 隨便打字後，好傑寶會跳出介面讓使用者繼續：

![](https://i.imgur.com/8vY7Suo.png)

* 這是主介面選單：

![image](https://user-images.githubusercontent.com/46813276/147872543-12360646-0c1a-4404-a008-c521b9e174e5.png)

* 點選好傑寶後的選單：

![image](https://user-images.githubusercontent.com/46813276/147872558-f15554fb-c5a8-4c7b-bb12-b4ab3bd417d2.png)

### 獲取最新影片
* 點入獲取最新影片後，會有三種選項：

![image](https://user-images.githubusercontent.com/46813276/147872606-5c067bd0-3577-45e8-b86c-12f32bc2baf0.png)

* 「一個」：好傑寶會回覆你一個羅傑最新影片的連結。
* 「五個」：好傑寶會回覆你五個羅傑最新影片的連結。
* 「我是來倒讚的」：好傑寶會叫你冷靜。
* 選五個的情況：

![image](https://user-images.githubusercontent.com/46813276/147872641-50465671-6a03-4d57-9a1c-6b178722933d.png)

按下「沒料，請你離開」或是「確實」，好傑寶就會回去上一步囉！

* 選「我是來倒讚的」：

![image](https://user-images.githubusercontent.com/46813276/147872670-b6e6c9b5-d991-43ad-8d50-36317a6382e6.png)

### 隨機抽羅傑梗圖

好傑寶會從GoogleSheet試算表裡的梗圖資料庫，隨機抽一個梗圖回應你：

![image](https://user-images.githubusercontent.com/46813276/147872718-8bdc3440-c6c7-49a3-a7e3-0243364c50f9.png)

* 選擇「再碰」：好傑寶會再進到相同的狀態，再抽一次梗圖回你。
* 選擇「沒料，請你離開」：會回到上一步。

### 書籤與資料管理
* 提供試算表資料的管理功能(如查看、新增、移除資料，與試算表網址連結)：

![image](https://user-images.githubusercontent.com/46813276/147872829-30de734d-a46a-438e-8f13-bb6f05aaf77a.png)

* 「**查看最愛影片**」：好傑寶會秀出資料庫裡所有的最愛影片連結：  
![image](https://user-images.githubusercontent.com/46813276/147873022-044334a7-89bd-4c0c-8d11-c232bd8a54ca.png)  
* 「新增最愛影片」：好傑寶會請你輸入一個網址，用**正規表達式**檢查是否為YT影片，並確認資料庫無相同網址後，就幫你更新到試算表中：  
![image](https://user-images.githubusercontent.com/46813276/147873042-a3a8b2c0-40aa-452f-92a9-e15cb5c1a089.png)
![image](https://user-images.githubusercontent.com/46813276/147873068-4874b11b-279c-4aed-a12d-0ad3e29982d4.png)  
****
![image](https://user-images.githubusercontent.com/46813276/147873088-2e31b743-dc37-40b4-9fff-258a67647a88.png)
![image](https://user-images.githubusercontent.com/46813276/147873123-47e65ea2-18ee-4cb4-8b6c-edcd32836deb.png)  
  ****
* 「**移除最愛影片**」：好傑寶會請你輸入一個網址，在試算表搜尋到相同的網址後，就幫你把它從試算表移除：  
![image](https://user-images.githubusercontent.com/46813276/147873146-c09cafcd-cdf8-4be7-b970-784b9d7b7d0f.png)
![image](https://user-images.githubusercontent.com/46813276/147873153-ce2f1f61-9f89-44ab-b02e-e95bb1653043.png)
  ****
* 「查看所有梗圖」：好傑寶會秀出資料庫裡所有的梗圖：  
![image](https://user-images.githubusercontent.com/46813276/147873281-06874833-8ff6-4c65-8176-3ff742532d64.png)
![image](https://user-images.githubusercontent.com/46813276/147873272-af5261d6-a28f-4396-a520-62e623cb038f.png)
  ****
* 「新增梗圖」：好傑寶會請你輸入一個imgur網址，用**正規表達式**檢查是否符合規定，再幫你更新到試算表中。
* 「移除梗圖」：好傑寶會請你輸入一個imgur網址，在試算表搜尋到相同的網址後，就幫你把它從試算表移除。
* 「給我資料庫連結！」：好傑寶會回應你試算表的網址，讓你可以觀察與手動修改。
* 「回到上一步」：好傑寶會讓你回去上一個選單。  
## FSM狀態圖  
![fsm](https://user-images.githubusercontent.com/46813276/147873321-e7829007-e918-4def-bc49-eb207c50b654.png)


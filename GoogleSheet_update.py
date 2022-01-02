import gspread
import random
import re
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path = 'gs.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表
spreadsheet_key = '1ssBedfSQYLVlz-vIbT1-EjUq9HsZ4_QtHrK3Pavl4WM' 
#建立工作表API
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

#alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N']
def roger_image():
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的梗圖")
    except:
        index = -1
        return False
    
    #取得目前的梗圖總數
    word = sheet.cell(2 , index+1).value
    if(word != None):
        word_list = word.split(':')
        if(len(word_list)>1):
            number = int(word_list[1])
    if(number>0):
        img_id = random.randint(1 , number)
        return sheet.cell(img_id+2 , index+1).value
    else:
        return "None"
def match_youtube_url(url):
    m1 = re.match(r'^(https?:\/\/)?(www\.)?(youtu\.be\/|youtube\.com\/(watch\?v=|watch\?.+))' , url)
    if(m1 is None):
        return False
    else:
        return True
def match_imgur_url(url):
    m1 = re.match(r'^(https?:\/\/)?i\.imgur\.com\/.+\.(jpg|png)' , url)
    if(m1 is None):
        return False
    else:
        return True
def add_imgur_url(url):
    if(match_imgur_url(url) == False):
        return False

    
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的梗圖")
    except:
        index = -1
        return False
    
    #取得目前的梗圖總數
    word = sheet.cell(2 , index+1).value
    if(word != None):
        word_list = word.split(':')
        if(len(word_list)>1):
            number = int(word_list[1])
            
    #確認是否已有相同網址存在
    url_list = sheet.col_values(index+1)[2:]   
    for exist_url in url_list:
        if(url == exist_url):
            return False
    #新增網址到試算表，並更新梗圖總數
    
    sheet.update_cell(3 + number, index+1, url)   
    number += 1
    word = '梗圖總數:' + str(number)
    sheet.update_cell(2 , index+1 , word)
    return True

def del_imgur_url(url):
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的梗圖")
    except:
        index = -1
        return False
    #取得目前的影片總數
    word = sheet.cell(2 , index+1).value
    if(word != None):
        word_list = word.split(':')
        if(len(word_list)>1):
            number = int(word_list[1])
    #開始尋找並刪除相同的url
    url_list = sheet.col_values(index+1)   
    if url in url_list:
        url_list.remove(url)
        url_list.append('')
        url_list[1] = '梗圖總數:' + str(number-1)
        for i , word in enumerate(url_list):
            sheet.update_cell(i+1 , index+1 , word)
        return True
    else:
        return False

def get_favorite_imgur_url():

    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的梗圖")
    except:
        index = -1
        return False
    # 讀取梗圖連結的那一整行
    
    return sheet.col_values(index+1)[2:]
def add_url(url):
    if(match_youtube_url(url) == False):
        return False
    
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的影片連結")
    except:
        index = -1
        return False
    #取得目前的影片總數
    word = sheet.cell(2 , index+1).value
    if(word != None):
        word_list = word.split(':')
        if(len(word_list)>1):
            number = int(word_list[1])
            
    #確認是否已有相同網址存在
    url_list = sheet.col_values(index+1)[2:]   
    for exist_url in url_list:
        if(url == exist_url):
            return False
    #新增網址到試算表，並更新影片總數
    
    sheet.update_cell(3 + number, index+1, url)   
    number += 1
    word = '影片總數:' + str(number)
    sheet.update_cell(2 , index+1 , word)
    return True
    # sheet.update_acell('D2', 'ABC')  #D2加入ABC
    # sheet.update_cell(2, 4, 'ABC')   #D2加入ABC(第2列第4行即D2)
    #寫入一整列(list型態的資料)
    # values = ['A','B','C','D']
    # sheet.insert_row(values, 1) #插入values到第1列
    #讀取儲存格
    # sheet.acell('B1').value
    # sheet.cell(1, 2).value
    #讀取整欄或整列
    # print(index)
    # sheet.col_values(1) #讀取第1欄的一整欄
    #讀取整個表
    # sheet.get_all_values()

def del_url(url):
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的影片連結")
    except:
        index = -1
        return False
    #取得目前的影片總數
    word = sheet.cell(2 , index+1).value
    if(word != None):
        word_list = word.split(':')
        if(len(word_list)>1):
            number = int(word_list[1])
    #開始尋找並刪除相同的url
    url_list = sheet.col_values(index+1)   
    if url in url_list:
        url_list.remove(url)
        url_list.append('')
        url_list[1] = '影片總數:' + str(number-1)
        for i , word in enumerate(url_list):
            sheet.update_cell(i+1 , index+1 , word)
        return True
    else:
        return False
def get_favorite_url():
   
    List = sheet.row_values(1) #讀取第1列的一整列
    try:
        index = List.index("儲存的影片連結")
    except:
        index = -1
        return False
    # 讀取影片連結的那一整行
    
    return sheet.col_values(index+1)[2:]
    
if __name__ == "__main__":
    print(roger_image())
    # print(delete_url(word))
    
    
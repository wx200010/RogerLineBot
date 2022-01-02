from transitions.extensions import GraphMachine

import os
import sys

from utils import send_text_message
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage , ImageSendMessage

from crawler import roger_getLink
import message
import GoogleSheet_update 


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "馬上來"  or text == "跟不上我的速度吧阿嘎"

    def is_going_to_show_fsm(self, event):
        text = event.message.text
        return text == "顯示FSM"

    def is_going_to_roger(self, event):
        text = event.message.text
        return text.lower() == "我是好傑寶" or text == "回到上一步" or text.lower() == "不留念了" or text.lower() == "沒料，請你離開" or text.lower() == "冷靜一下" or text.lower() == "確實"
    def is_going_to_roger_database(self, event):
        text = event.message.text
        # 回覆目前已儲存的的所有連結
        if(text == "查看最愛影片"):

            userid = event.source.user_id 
            line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
            line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
            url_list = GoogleSheet_update.get_favorite_url()
            if(len(url_list) != 0):
                line_bot_api.push_message(userid, TextSendMessage("已儲存的最愛影片："))
                for word in url_list:
                    line_bot_api.push_message(userid, TextSendMessage(word))
            else:
                line_bot_api.push_message(userid, TextSendMessage("目前沒有儲存任何影片!!"))
        # 回覆目前已儲存的的所有梗圖
        elif(text == "查看所有梗圖"):

            userid = event.source.user_id 
            line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
            line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
            url_list = GoogleSheet_update.get_favorite_imgur_url()
            if(len(url_list) != 0):
                for word in url_list:
                    line_bot_api.push_message(userid, ImageSendMessage(word , word))
            else:
                line_bot_api.push_message(userid, TextSendMessage("目前沒有儲存任何梗圖!!"))
        elif (text == "給我資料庫連結!"):
            userid = event.source.user_id 
            line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
            line_bot_api.push_message(userid, TextSendMessage("https://docs.google.com/spreadsheets/d/1ssBedfSQYLVlz-vIbT1-EjUq9HsZ4_QtHrK3Pavl4WM/edit#gid=0"))
    
        return text.lower() == "書籤與資料管理" or text == "查看最愛影片" or text == "給我資料庫連結!" or text == "查看所有梗圖"
    
    def from_add_url_to_roger_database(self, event):
        url = event.message.text
        userid = event.source.user_id 
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
        #開始更新最愛清單
        if(GoogleSheet_update.add_url(url) == True):       
            line_bot_api.push_message(userid, TextSendMessage(text = "成功更新最愛清單!"))    
        else:
            line_bot_api.push_message(userid, TextSendMessage(text = "更新失敗，請確認是否已有相同網址，或是該連結並非youtube影片連結。"))
        return True    
    
    def from_del_url_to_roger_database(self, event):
        url = event.message.text
        userid = event.source.user_id 
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
        #開始更新最愛清單
        if(GoogleSheet_update.del_url(url) == True):       
            line_bot_api.push_message(userid, TextSendMessage(text = "成功更新最愛清單!"))    
        else:
            line_bot_api.push_message(userid, TextSendMessage(text = "更新失敗，請確認是否已有相同網址，或是該連結並非youtube影片連結。"))
        return True    
    def from_add_imgur_url_to_roger_database(self, event):
        url = event.message.text
        userid = event.source.user_id 
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
        #開始更新最愛清單
        if(GoogleSheet_update.add_imgur_url(url) == True):       
            line_bot_api.push_message(userid, TextSendMessage(text = "成功更新梗圖清單!"))    
        else:
            line_bot_api.push_message(userid, TextSendMessage(text = "更新失敗，請確認是否已有相同網址，或是該連結並非imgur連結 (例：i.imgur.com/XXXXXX.png)。"))
        return True    
    
    def from_del_imgur_url_to_roger_database(self, event):
        url = event.message.text
        userid = event.source.user_id 
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage("處理中，請稍後..."))
        #開始更新最愛清單
        if(GoogleSheet_update.del_imgur_url(url) == True):       
            line_bot_api.push_message(userid, TextSendMessage(text = "成功更新梗圖清單!"))    
        else:
            line_bot_api.push_message(userid, TextSendMessage(text = "更新失敗，請確認是否已有相同網址，或是該連結並非imgur連結 (例：i.imgur.com/XXXXXX.png)。"))
        return True
    
    def is_going_to_roger_database_add_url(self, event):
        text = event.message.text
        return text == "新增最愛影片" 
    def is_going_to_roger_database_del_url(self, event):
        text = event.message.text
        return text == "移除最愛影片" 
    def is_going_to_roger_database_add_imgur_url(self, event):
        text = event.message.text
        return text == "新增梗圖" 
    def is_going_to_roger_database_del_imgur_url(self, event):
        text = event.message.text
        return text == "移除梗圖" 
    
    def is_going_to_roger_video(self, event):
        text = event.message.text
        return text.lower() == "看看最新影片"
    def is_going_to_roger_image(self, event):
        text = event.message.text
        return text.lower() == "鬼抽" or text.lower() == "再碰"
    def is_going_to_roger_video1(self, event):
        text = event.message.text
        return text.lower() == "一個"
    def is_going_to_roger_video5(self, event):
        text = event.message.text
        return text.lower() == "五個"
    def is_going_to_roger_bad(self, event):
        text = event.message.text
        return text.lower() == "我是來倒讚的"

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message_block = message.main_menu
        to_reply = FlexSendMessage("這是主選單", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, to_reply)
        
    def on_enter_show_fsm(self, event):
        userid = event.source.user_id
        message_block = message.show_fsm_menu
        to_reply = FlexSendMessage("回上一步", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, ImageSendMessage("https://i.imgur.com/21yz2fS.png" , "https://i.imgur.com/21yz2fS.png"))
        line_bot_api.push_message(userid, to_reply)
        
        
    def on_enter_roger(self, event):
        reply_token = event.reply_token
        message_block = message.roger_menu
        to_reply = FlexSendMessage("傑寶菜單", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, to_reply)
    
    def on_enter_roger_video(self, event):
        reply_token = event.reply_token
        message_block = message.roger_video_ask
        to_reply = FlexSendMessage("抽影片", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, to_reply)
        
    def on_enter_roger_image(self, event):
        userid = event.source.user_id
        
        image_path = GoogleSheet_update.roger_image()    

        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, ImageSendMessage(image_path , image_path))
        message_block = message.roger_image_back
        to_reply = FlexSendMessage("回主選單", message_block)
        line_bot_api.push_message(userid, to_reply)
    
    def on_enter_roger_database(self, event):
        reply_token = event.reply_token
        message_block = message.roger_database_menu
        to_reply = FlexSendMessage("資料庫管理", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, to_reply)
        
    def on_enter_roger_database_add_url(self, event):
        userid = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = "請告訴我影片連結~"))
        
    def on_enter_roger_database_del_url(self, event):
        userid = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = "請告訴我影片連結~"))
        
    def on_enter_roger_database_add_imgur_url(self, event):
        userid = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = "請告訴我梗圖連結~ "))
        
    def on_enter_roger_database_del_imgur_url(self, event):
        userid = event.source.user_id
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, TextSendMessage(text = "請告訴我梗圖連結~ "))
        
    def on_enter_roger_video1(self, event):
        userid = event.source.user_id
        reply_token = event.reply_token
        
        video_links =  roger_getLink(1)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, TextSendMessage(text = video_links[0]))
        message_block = message.roger_video_back
        to_reply = FlexSendMessage("回主選單", message_block)
        line_bot_api.push_message(userid, to_reply)
        
    def on_enter_roger_video5(self, event):
        userid = event.source.user_id
        reply_token = event.reply_token
        
        video_links =  roger_getLink(5)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        for link in video_links:
            line_bot_api.push_message(userid, TextSendMessage(text = link))
        message_block = message.roger_video_back
        to_reply = FlexSendMessage("回主選單", message_block)
        line_bot_api.push_message(userid, to_reply)
        
    def on_enter_roger_bad(self, event):
        reply_token = event.reply_token
        userid = event.source.user_id
        message_block = message.roger_bad_back
        to_reply = FlexSendMessage("傑寶菜單", message_block)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, TextSendMessage(text = "你冷靜點"))
        line_bot_api.push_message(userid, to_reply)
        
    def on_enter_end(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger end")
        self.go_back()


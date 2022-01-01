from transitions.extensions import GraphMachine

import os
import sys

from utils import send_text_message
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage , ImageSendMessage
from message import roger_image
from crawler import roger_getLink
import message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "馬上來" or text.lower() == "不留念了" or text.lower() == "沒料，請你離開" or text.lower() == "冷靜一下"

    def is_going_to_roger(self, event):
        text = event.message.text
        return text.lower() == "我是好傑寶"
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
        
        image_path = roger_image()    

        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.push_message(userid, ImageSendMessage(image_path , image_path))
        message_block = message.roger_image_back
        to_reply = FlexSendMessage("回主選單", message_block)
        line_bot_api.push_message(userid, to_reply)
    
        
    def on_enter_roger_video1(self, event):
        userid = event.source.user_id
        reply_token = event.reply_token
        
        video_links =  roger_getLink(1)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        line_bot_api.reply_message(reply_token, TextSendMessage(text = video_links[0]))
        message_block = message.roger_image_back
        to_reply = FlexSendMessage("回主選單", message_block)
        line_bot_api.push_message(userid, to_reply)
        
    def on_enter_roger_video5(self, event):
        userid = event.source.user_id
        reply_token = event.reply_token
        
        video_links =  roger_getLink(5)
        line_bot_api = LineBotApi( os.getenv('LINE_CHANNEL_ACCESS_TOKEN') )
        for link in video_links:
            line_bot_api.push_message(userid, TextSendMessage(text = link))
        message_block = message.roger_image_back
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


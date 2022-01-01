import random
def roger_image():
  image_path = [  "https://i.imgur.com/Agp2S9F.jpg",  "https://i.imgur.com/bvBn2AK.jpg", 
            "https://i.imgur.com/8SGpZ2j.jpg",  "https://i.imgur.com/fvxJumE.jpg",
            "https://i.imgur.com/XmSWT4E.jpg",  "https://i.imgur.com/PRF2Jpo.jpg",
            "https://i.imgur.com/YLRYmVR.jpg",  "https://i.imgur.com/XevIv2p.jpg",
            "https://i.imgur.com/q1SxDfa.jpg",  "https://i.imgur.com/wNoxn7h.jpg",
            "https://i.imgur.com/Sgr4wK1.jpg",  "https://i.imgur.com/XevIv2p.jpg",
            "https://i.imgur.com/XmSWT4E.jpg",  "https://i.imgur.com/txD2qZ4.jpg",
            "https://i.imgur.com/rNFffqR.jpg",  "https://i.imgur.com/zgN6vWV.jpg",
            "https://i.imgur.com/9gQjDWG.jpg",  "https://i.imgur.com/Lrduxrr.jpg",
            "https://i.imgur.com/L96pS1C.jpg",  "https://i.imgur.com/sj17DoY.jpg"
          ]
  img_id = random.randint(0 , len(image_path)-1)
  
  return image_path[img_id]

user_start =  {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "點我進入主選單",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "馬上來",
              "text": "馬上來"
            },
            "height": "md",
            "color": "#00d13b",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

main_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/ubLffKT.jpg",
        "size": "full",
        "aspectMode": "fit",
        "aspectRatio": "1.25:1"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "好傑寶功能",
              "text": "我是好傑寶"
            },
            "height": "md",
            "color": "#ff9900",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

roger_menu = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "好傑寶的功能列~",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "看看最新影片",
              "text": "看看最新影片"
            },
            "height": "md",
            "color": "#01B468",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "梗圖抽抽樂",
              "text": "鬼抽"
            },
            "height": "md",
            "color": "#01c673",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}
roger_video_ask = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "要獲得多少個影片連結呢?",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "一個",
              "text": "一個"
            },
            "height": "md",
            "color": "#00d13b",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "五個",
              "text": "五個"
            },
            "height": "md",
            "color": "#00cc66",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "我是來倒讚的",
              "text": "我是來倒讚的"
            },
            "height": "md",
            "color": "#eac100",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}


roger_image_back = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "還行吧聊天室",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "再碰一張",
              "text": "再碰"
            },
            "height": "md",
            "color": "#00c219",
            "style": "primary"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "沒料，請你離開",
              "text": "沒料，請你離開"
            },
            "height": "md",
            "color": "#5bc200",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      },
    }
  ]
}
roger_back = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "點我返回主選單",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "不留念了",
              "text": "不留念了"
            },
            "height": "md",
            "color": "#00EC00",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}

roger_bad_back = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "你冷靜點",
            "weight": "bold",
            "align": "center",
            "size": "lg"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "去冷靜",
              "text": "冷靜一下"
            },
            "height": "md",
            "color": "#00c200",
            "style": "primary"
          }
        ],
        "spacing": "lg"
      }
    }
  ]
}
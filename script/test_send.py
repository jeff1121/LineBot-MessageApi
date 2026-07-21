import requests
import json
import time

URL = "http://localhost:3000/webhook"
HEADERS = {
    "Content-Type": "application/json",
    "x-line-signature": "dummy-signature"
}

def send_payload(name, payload):
    print(f"\n--- 測試: {name} ---")
    try:
        response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))
        print(f"HTTP Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

# 測試範例 1: 文字訊息 (Text Message)
payload_text = {
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "text",
                "id": "14353798921116",
                "text": "Hello, world"
            },
            "timestamp": int(time.time() * 1000),
            "source": {
                "type": "user",
                "userId": "U80696558e1aa831..."
            },
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA"
        }
    ]
}

# 測試範例 2: 貼圖訊息 (Sticker Message)
payload_sticker = {
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "sticker",
                "id": "14353798921116",
                "packageId": "1",
                "stickerId": "1"
            },
            "timestamp": int(time.time() * 1000),
            "source": {
                "type": "user",
                "userId": "U80696558e1aa831..."
            },
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA"
        }
    ]
}

# 測試範例 3: 圖片訊息 (Image Message)
payload_image = {
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "image",
                "id": "325708"
            },
            "timestamp": int(time.time() * 1000),
            "source": {
                "type": "user",
                "userId": "U80696558e1aa831..."
            },
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA"
        }
    ]
}

# 測試範例 4: 加入好友事件 (Follow Event)
payload_follow = {
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "follow",
            "timestamp": int(time.time() * 1000),
            "source": {
                "type": "user",
                "userId": "U80696558e1aa831..."
            },
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA"
        }
    ]
}

# 測試範例 5: 按鈕回應事件 (Postback Event)
payload_postback = {
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "postback",
            "postback": {
                "data": "action=buy&itemid=123"
            },
            "timestamp": int(time.time() * 1000),
            "source": {
                "type": "user",
                "userId": "U80696558e1aa831..."
            },
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA"
        }
    ]
}

if __name__ == "__main__":
    send_payload("文字訊息", payload_text)
    send_payload("貼圖訊息", payload_sticker)
    send_payload("圖片訊息", payload_image)
    send_payload("加入好友事件", payload_follow)
    send_payload("按鈕回應事件", payload_postback)

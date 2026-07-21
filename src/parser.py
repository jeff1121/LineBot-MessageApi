from typing import Optional
from models import LineSource, LineMessage, LineEvent, LineWebhookPayload

def parse_webhook_payload(payload_dict: dict) -> LineWebhookPayload:
    """
    將傳入的原始 JSON 字典解析為 LineWebhookPayload 及強型別 Dataclass 物件。
    """
    destination = payload_dict.get("destination", "")
    events_data = payload_dict.get("events", [])
    
    events = []
    for evt_data in events_data:
        # 解析訊息來源
        source_data = evt_data.get("source", {})
        source = LineSource(
            type=source_data.get("type", "unknown"),
            user_id=source_data.get("userId"),
            group_id=source_data.get("groupId"),
            room_id=source_data.get("roomId")
        )
        
        # 解析訊息內容
        message_data = evt_data.get("message")
        message = None
        if message_data:
            message = LineMessage(
                id=message_data.get("id", ""),
                type=message_data.get("type", "unknown"),
                text=message_data.get("text"),
                title=message_data.get("title"),
                address=message_data.get("address"),
                latitude=message_data.get("latitude"),
                longitude=message_data.get("longitude"),
                package_id=message_data.get("packageId"),
                sticker_id=message_data.get("stickerId"),
                content_provider=message_data.get("contentProvider")
            )
            
        # 解析 postback 資料
        postback_data = evt_data.get("postback", {}).get("data")
        
        # 解析重發上下文 (deliveryContext)
        delivery_context = evt_data.get("deliveryContext", {})
        is_redelivery = delivery_context.get("isRedelivery", False)
        
        event = LineEvent(
            type=evt_data.get("type", "unknown"),
            mode=evt_data.get("mode", "active"),
            timestamp=evt_data.get("timestamp", 0),
            source=source,
            webhook_event_id=evt_data.get("webhookEventId", ""),
            delivery_context_is_redelivery=is_redelivery,
            reply_token=evt_data.get("replyToken"),
            message=message,
            postback_data=postback_data
        )
        events.append(event)
        
    return LineWebhookPayload(destination=destination, events=events)

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class LineSource:
    """LINE 訊息/事件的來源模型 (User / Group / Room)"""
    type: str
    user_id: Optional[str] = None
    group_id: Optional[str] = None
    room_id: Optional[str] = None

@dataclass
class LineMessage:
    """LINE 訊息物件模型 (Text, Sticker, Image, Video, Audio, Location 等)"""
    id: str
    type: str
    text: Optional[str] = None
    title: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    package_id: Optional[str] = None
    sticker_id: Optional[str] = None
    content_provider: Optional[dict] = None

@dataclass
class LineEvent:
    """LINE Webhook 事件模型"""
    type: str
    mode: str
    timestamp: int
    source: LineSource
    webhook_event_id: str
    delivery_context_is_redelivery: bool
    reply_token: Optional[str] = None
    message: Optional[LineMessage] = None
    postback_data: Optional[str] = None

@dataclass
class LineWebhookPayload:
    """LINE Webhook 完整推送資料結構"""
    destination: str
    events: List[LineEvent]

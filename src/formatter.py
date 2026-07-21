from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.text import Text
from models import LineWebhookPayload

console = Console()

def print_webhook_events(payload: LineWebhookPayload):
    """
    使用 Rich Console 於終端機繪製表格，展示 Webhook 事件明細。
    """
    if not payload.events:
        console.print("[yellow]收到空的 Webhook 事件。[/yellow]")
        return

    table = Table(title="LINE Webhook 事件列表", show_header=True, header_style="bold magenta")
    table.add_column("時間", justify="left")
    table.add_column("事件類型", justify="center")
    table.add_column("來源", justify="left")
    table.add_column("訊息與詳細內容", justify="left")
    table.add_column("Reply Token", justify="left", overflow="fold")
    table.add_column("Webhook Event ID", justify="left", overflow="fold")

    for event in payload.events:
        # 時間轉換
        try:
            dt = datetime.fromtimestamp(event.timestamp / 1000.0)
            time_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            time_str = str(event.timestamp)

        # 事件類型與顏色樣式
        event_type = event.type
        type_text = Text(event_type.capitalize())
        if event_type == "message":
            type_text.stylize("bold green")
        elif event_type in ("follow", "unfollow"):
            type_text.stylize("bold blue")
        elif event_type == "postback":
            type_text.stylize("bold yellow")
        elif event_type == "join":
            type_text.stylize("bold cyan")

        # 來源資訊
        source_str = f"{event.source.type.capitalize()}"
        if event.source.type == "user" and event.source.user_id:
            source_str += f"\nID: {event.source.user_id}"
        elif event.source.type == "group" and event.source.group_id:
            source_str += f"\nID: {event.source.group_id}"
        elif event.source.type == "room" and event.source.room_id:
            source_str += f"\nID: {event.source.room_id}"

        # 訊息摘要與詳細資訊
        details = ""
        if event.type == "message" and event.message:
            msg = event.message
            details = f"[{msg.type.capitalize()}]\n"
            if msg.type == "text":
                details += msg.text or ""
            elif msg.type == "sticker":
                details += f"Pkg: {msg.package_id}, Sticker: {msg.sticker_id}"
            elif msg.type in ("image", "video", "audio"):
                details += f"MsgID: {msg.id}"
            elif msg.type == "location":
                details += f"{msg.title}\n{msg.address}"
        elif event.type == "postback" and event.postback_data:
            details = f"Data: {event.postback_data}"

        table.add_row(
            time_str,
            type_text,
            source_str,
            details,
            event.reply_token or "-",
            event.webhook_event_id or "-"
        )

    console.print(table)

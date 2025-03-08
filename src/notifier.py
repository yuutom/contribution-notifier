import requests
import json
import os


def send_message(channel_access_token, user_id, message):
    """
    LINE公式アカウントを使ってメッセージを送信する

    :param channel_access_token: LINE Messaging APIのチャネルアクセストークン
    :param user_id: 送信先のLINEユーザーID
    :param message: 送信するメッセージ
    """
    if not channel_access_token or not user_id:
        raise ValueError("LINE Channel Token and User ID must be provided.")

    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {channel_access_token}"
    }

    payload = {
        "to": user_id,
        "messages": [{"type": "text", "text": message}]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"LINE API Error: {response.text}")

    return response.status_code

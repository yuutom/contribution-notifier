import requests


def send_notification(line_token, message):
    if not line_token:
        raise ValueError("LINE Notify token is not provided.")

    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {line_token}"}
    payload = {"message": message}

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception(f"Notification failed: {response.text}")

    return response.status_code

import json
from lambda_function import lambda_handler

if __name__ == "__main__":
    event = {}  # 必要ならここにパラメータを設定
    response = lambda_handler(event, None)
    print(json.dumps(response, indent=2))

import os
import json
import requests
import sys

def fetch_panopto_info(delivery_id):
    url = "https://polyu.ap.panopto.com/Panopto/Pages/Viewer/DeliveryInfo.aspx"

    # POST 的 form-data
    payload = {
        "deliveryId": delivery_id,
        "getCaptions": "true",
        "language": "0",
        "responseType": "json"
    }

    response = requests.post(url, data=payload)

    # 创建 data 目录
    os.makedirs("RAWJson", exist_ok=True)

    # 输出文件路径
    output_path = f"RAWJson/{delivery_id}.json"

    # 保存 JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=2)

    print(f"已保存到 {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python save_panopto.py <deliveryId>")
        sys.exit(1)

    delivery_id = sys.argv[1]
    fetch_panopto_info(delivery_id)

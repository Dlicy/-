import sys
import base64
import hashlib
import hmac
import json
import os
import time
import requests

class RequestApi:
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.lfasr_host = "http://raasr.xfyun.cn/api"
        self.api_upload = "/v1/service/v1/lfasr/upload"
        self.api_get_result = "/v1/service/v1/lfasr/getResult"

    def get_signa(self, ts):
        signa = hmac.new(self.secret_key.encode('utf-8'), '{}{}{}'.format(self.appid, ts, 'r6x2Z0oJp5RQ7D7p').encode('utf-8'), digestmod=hashlib.sha256).hexdigest()
        return signa

    def upload(self):
        file_size = os.path.getsize(self.upload_file_path)
        file_name = os.path.basename(self.upload_file_path)
        ts = str(int(time.time()))
        signa = self.get_signa(ts)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        data = {
            'app_id': self.appid,
            'signa': signa,
            'ts': ts,
            'file_len': str(file_size),
            'file_name': file_name
        }
        url = self.lfasr_host + self.api_upload
        try:
            res = requests.post(url, headers=headers, data=data, files={'file': open(self.upload_file_path, 'rb')})
            result = json.loads(res.text)
            return result['data']['task_id']
        except Exception as e:
            print("Error occurred during upload:", e)
            return None

    def get_result(self, task_id):
        ts = str(int(time.time()))
        signa = self.get_signa(ts)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        data = {
            'app_id': self.appid,
            'signa': signa,
            'ts': ts,
            'task_id': task_id
        }
        url = self.lfasr_host + self.api_get_result
        while True:
            try:
                res = requests.post(url, headers=headers, data=data)
                result = json.loads(res.text)
                if result['data']['status'] == 9:
                    return result['data']['lfasr_text']
                else:
                    time.sleep(2)
            except Exception as e:
                print("Error occurred during getting result:", e)
                return None

def transcribe_audio_file(file_path, appid, secret_key):
    transcriber = RequestApi(appid, secret_key, file_path)
    task_id = transcriber.upload()
    if task_id:
        result = transcriber.get_result(task_id)
        return result
    else:
        return None

# 使用示例
if __name__ == "__main__":
    appid = "your_appid"
    secret_key = "your_secret_key"
    file_path = sys.argv[1] if len(sys.argv) > 1 else None
    if file_path:
        transcription = transcribe_audio_file(file_path, appid, secret_key)
        if transcription:
            with open("transcription.txt", "w", encoding="utf-8") as file:
                file.write(transcription)
            print("Transcription saved to transcription.txt")
        else:
            print("Transcription failed")
    else:
        print("No file name provided")

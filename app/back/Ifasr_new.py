import sys
import base64
import hashlib
import hmac
import json
import os
import time
import requests
import urllib

# 获取命令行参数，即上传的文件路径
if len(sys.argv) > 1:
    upload_file_path = sys.argv[1]
    print("Received file:", upload_file_path)
else:
    print("No file name provided")


lfasr_host = 'https://raasr.xfyun.cn/v2/api'
# 请求的接口名
api_upload = '/upload'
api_get_result = '/getResult'


class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.ts = str(int(time.time()))
        self.signa = self.get_signa()

    def get_signa(self):
        appid = self.appid
        secret_key = self.secret_key
        m2 = hashlib.md5()
        m2.update((appid + self.ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        return signa


    def upload(self):
        print("上传部分：")
        upload_file_path = self.upload_file_path
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict["fileSize"] = file_len
        param_dict["fileName"] = file_name
        param_dict["duration"] = "200"
#        print("upload参数：", param_dict)
        data = open(upload_file_path, 'rb').read(file_len)
        res = urllib.parse.urlencode(param_dict)
#        print(lfasr_host + api_upload+"?"+urllib.parse.urlencode(param_dict))
        response = requests.post(url =lfasr_host + api_upload+"?"+urllib.parse.urlencode(param_dict),
                                 headers = {"Content-type":"application/json"},data=data)
#        print("upload_url:",response.request.url)
        result = json.loads(response.text)
#        print("upload resp:", result)
        return result


    def get_result(self):
        uploadresp = self.upload()
        orderId = uploadresp['content']['orderId']
        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict['orderId'] = orderId
        param_dict['resultType'] = "transfer,predict"
        print("")
        print("查询部分：")
        #print("get result参数：", param_dict)
        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            response = requests.post(url=lfasr_host + api_get_result + "?" + urllib.parse.urlencode(param_dict),
                                     headers={"Content-type": "application/json"})
            #print("get_result_url:",response.request.url)
            result = json.loads(response.text)
            #return result
            #print(result)
            status = result['content']['orderInfo']['status']
            #print("status=",status)
            if status == 4:
                break
            time.sleep(5)
        #print("get_result resp:",result)
        return result
        return urllib.parse.urlencode(param_dict)




# 输入讯飞开放平台的appid，secret_key和待转写的文件路径

# 输入讯飞开放平台的 appid，secret_key 和待转写的文件路径
api = RequestApi(appid="3efb053a",
                 secret_key="3152fc469900fe3f11ed6bbf017872ed",
                 upload_file_path=upload_file_path)
print(1)
#test1 = api.get_result()['orderResult']
#json_data = test1["orderResult"]
#data = json.loads(api.get_result())
#order_info = api.get_result()['content']['orderInfo']
order_result = json.loads(api.get_result()['content']['orderResult'])
#print(test1)
#print(order_info)
#print(order_result)
#print(type(api.get_result()))
# for value in api.get_result():
#     print(value)
# lattice = order_result["lattice"]
# lattice2 = order_result["lattice2"]

# 解析数据
json_data = json.loads(order_result['lattice'][0]['json_1best'])

# 提取文本
text = ''.join([cw['w'] for rt in json_data['st']['rt'] for ws in rt['ws'] for cw in ws['cw']])

# 处理文本（示例：打印文本）
print(text)

# 创建一个文本文件并保存查询结果
with open('data\query.txt', 'w', encoding='utf-8') as file:
    file.write(text)


# 打印成功保存的消息
print("查询结果已保存到 query_result.txt 文件中")
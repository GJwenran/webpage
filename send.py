import requests

# 服务器的URL（根据你的服务器地址进行调整）
url = 'http://127.0.0.1:5000/'  # 如果Flask在本地运行，则使用这个URL

# 准备上传的文件和描述
file_path = r'D:\wordoffice\pythonProject\static\ background.jpg'  # 这里填写你想要上传的图片的路径
description = 'This is a description of the image.'

# 打开图片文件
with open(file_path, 'rb') as file:
    # 构造要发送的数据，包括文件和描述
    files = {'file': file}
    data = {'description': description}

    # 发送POST请求到服务器
    response = requests.post(url, files=files, data=data)

# 输出服务器的响应内容
print(response.text)

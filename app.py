from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
# 如果文件夹不存在，则创建
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 检查是否有文件上传
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # 保存上传的文件
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)

            # 获取用户输入的文本内容
            description = request.form.get('description')

            # 重定向到结果页面，传递图片路径和描述文本
            return render_template('result.html', image_path=image_path, description=description)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

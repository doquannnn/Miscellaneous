from flask import Flask, render_template, request
from face_extraction import extract_face
from matching import face_matching
from random import random
import os


# Khởi tạo Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static"


# Hàm xử lý request


@app.route("/", methods=['GET', 'POST'])
def home_page():
    if request.method == "POST":
        try:
            image = request.files['file']
            image_path = os.path.join(
                app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            # có thể detect dc khuôn mặt hoặc không
            face = extract_face(image_path)

            if len(face) != 0:
                extra = face_matching(face)

                return render_template("index.html", user_image=image.filename, rand=str(random()),
                                       msg="Tải file lên thành công", idBoolean=True, extra=extra)
            else:
                return render_template('index.html', msg='Không nhận diện được khuôn mặt')

            return render_template('index.html')
        except Exception as ex:
            # Nếu lỗi thì thông báo
            print(ex)
            return render_template('index.html', msg='Không nhận diện được khuôn mặt')

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'),
            port=int(os.getenv('PORT', 5555)))

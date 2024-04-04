from flask import Flask, url_for, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__, template_folder="static/htmls")


@app.route('/')
def mission():
    return "<h2>Миссия Колонизация Марса</h2>"


@app.route('/index', methods=['GET'])
def index():
    return render_template("index.html")


@app.route('/promotion', methods=['GET'])
def promotion():
    return render_template("promotion.html")


@app.route('/image_mars')
def image_mars():
    return render_template('image_mars.html')


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
    if request.method == 'POST':
        surname = request.form.get('surname')
        name = request.form.get('name')
        email = request.form.get('email')
        education = request.form.get('education')
        profession = request.form.get('profession')
        gender = request.form.get('gender')
        motivation = request.form.get('motivation')
        stay_on_mars = request.form.get('stay_on_mars')

        print(f"Фамилия: {surname}, Имя: {name}, Email: {email}, Образование: {education}, Профессия: {profession}, Пол: {gender}, Мотивация: {motivation}, Готовы ли остаться на Марсе: {stay_on_mars}")

        return "Данные успешно обработаны!"
    else:
        return render_template('astronaut_selection.html')


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return render_template('results.html', nickname=nickname, level=level, rating=rating)


@app.route('/photo/<nickname>', methods=['GET', 'POST'])
def photo_upload(nickname):
    if request.method == 'POST':
        photo = request.files['photo']
        photo.save(f'static/uploads/{photo.filename}')
        return redirect(url_for('photo_upload', nickname=nickname))
    return render_template('photo_upload.html', nickname=nickname)


@app.route('/carousel')
def carousel():
    images = ['mars1.jpg', 'mars2.jpg', 'mars3.jpg']
    return render_template('carousel.html', images=images)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
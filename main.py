from flask import Flask, render_template, redirect

from forms.user import RegisterForm, LoginForm
from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blog .db")
    app.run()


@app.route("/add_data")
def add_data():
    db_sess = db_session.create_session()

    # Добавление пользователей
    user = User()
    user.surname = "Scott"
    user.name = "Rdley"
    user.email = "scott_chief@mars.org"
    user.age = 21
    user.position = "capitan"
    user.speciality = "research engineer"
    user.address = "module_1"
    db_sess.add(user)
    print(user.email)

    for i in range(3):
        user = User()
        user.name = f"Пользователь {i+1}"
        user.surname = f" surname {i+1}"
        user.email = f"ggggggggggh{10*i+i}@email.ru"
        user.age = 1+i
        user.position = f" team {i + 1}"
        user.speciality = f"///{i + 1}"
        user.address = f"?{i + 1}"
        db_sess.add(user)
        print(user.email)

    print("cap and 3 col")
    # Добавление работ
    jobs = Jobs(job="Первая работа",work_size = 15,collaborators="2,3", team_leader=1, is_finished=False)
    db_sess.add(jobs)
    # # Несколько другой способ внесения связанных данных в БД
    # # user = db_sess.query(User).filter(User.id == 1).first()
    # # print(user)
    # jobs = Jobs(job="Вторая работа", collaborators="Ivanov", team_leader=2, is_finished=False)
    #
    # db_sess.add(jobs)
    print(jobs.job, "jobs.collaborators=", jobs.collaborators,"jobs.work_size =",jobs.work_size)
    db_sess.commit()
    return "Данные добавлены!<p><a href='.'>назад</a></p>"


@app.route("/select_data")
def select_data():
    db_sess = db_session.create_session()
    for user1 in db_sess.query(User).all():
        print(user1)
    for user2 in db_sess.query(User).filter(User.id > 1, User.email.notilike("%1%")):
        print(user2)
    return "Данные выбраны!<p><a href='.'>назад</a></p>"


@app.route("/delete_data")
def delete_data():
    db_sess = db_session.create_session()
    db_sess.query(User).filter(User.id >= 2).delete()
    db_sess.commit()
    return "Данные удалены!<p><a href='.'>назад</a></p>"


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).filter(Jobs.is_finished != True)
    return render_template("index.html", jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # for user in db_session.query(User).all():
    #     print(user)
    return render_template('login.html', title='Вход', form=form)


if __name__ == '__main__':
    main()

from flask import Flask, render_template, redirect
from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():

    db_name = input()

    db_session.global_init(db_name)
    app.run()
    db_sess = db_session.create_session()
    print("session in query1")

    # for user1 in db_sess.query(User).all():
    #     print(user1)

    for user1 in db_sess.query(User).filter(User.address.like("module_1")):
        print(user1)
#
# @app.route("/")
# def index():
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).filter(Jobs.is_finished != True)
#     return render_template("index.html", jobs=jobs)



if __name__ == '__main__':
    main()

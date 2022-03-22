from flask import Flask
from data.jobs import Jobs
from data.users import User
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'



def main():

    # db_name = input()

    db_session.global_init('db/new.db')
    app.run()
    db_sess = db_session.create_session()
    print("session in query1")

    for user1 in db_sess.query(User).all():
        print(user1)

    for user1 in db_sess.query(User).filter(User.address.like("module_1")):
        print(user1)



if __name__ == '__main__':
    main()

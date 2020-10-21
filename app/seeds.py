from app.models import Household, User, Event, Chore, Bill


def seed(db):
    # drop the current database and create a new database
    db.drop_all()
    db.create_all()

    household1 = Household(name='House1')
    household2 = Household(name='House2')

    user1 = User(name="Steven", email="fake@gmail.com", password="example", household=household1)
    user2 = User(name="Lisa", email="lisa@gmail.com", password="something", household=household2)
    user3 = User(name="Chris", email="chris@gmail.com", password="nothing", household=household1)

    # add seeds to the db session to prepare to commit
    db.session.add(household1)
    db.session.add(household2)
    
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    # save seeds to the database
    db.session.commit()
    print('Database seeded!')

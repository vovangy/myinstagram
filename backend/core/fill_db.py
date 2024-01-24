def main():
    Fake = Faker()
    moments_photo = ['images/1.png', 'images/2.png','images/3.png','images/4.png','images/5.png',
               'images/6.png','images/7.png','images/8.png','images/9.png','images/10.png',
               'images/11.png']
    '''users = []
    usernames = []
    emails = []
    for _ in range(1000):
        username = Fake.user_name()
        email = Fake.email()

        usernames.append(username)
        emails.append(email)

    usernames = list(set(usernames))
    emails = list(set(emails))

    for _ in range(min(len(usernames), len(emails))):
        username = usernames[_]
        email = emails[_]
        image_url = random.choice(moments_photo)
        password = 'A1b2C3d45'
        user = User(username=username, email=email, password=password, image_url=image_url)
        users.append(user)
    User.objects.bulk_create(users)'''

    '''users = User.objects.all()

    moments_photo = ['images/1.png', 'images/2.png','images/3.png','images/4.png','images/5.png',
               'images/6.png','images/7.png','images/8.png','images/9.png','images/10.png',
               'images/11.png']

    for i in range(10000):
        date = Fake.date_between()
        moments = []
        moment = Moment(user_id=User.objects.filter(id=random.randint(1, users.count()))[0],
                        title=Fake.text(max_nb_chars=random.randint(10, 30)),
                         content=Fake.text(max_nb_chars=random.randint(30, 250)),
                         image_url=random.choice(moments_photo),
                        pub_date=date)
        moments.append(moment)
        Moment.objects.bulk_create(moments)
    print(f"There are {users.count()} users in the database")'''
    '''users = User.objects.all()
    subscribers = []
    for _ in range(1000):
        author = User.objects.get(id=random.randint(1, users.count()))
        subscriber = User.objects.get(id=random.randint(1, users.count()))
        if author != subscriber:
            sub = Subscrition(user_id=author, subscriber_id=subscriber)
            subscribers.append(sub)
    Subscrition.objects.bulk_create(subscribers)''';
    users = User.objects.all()
    moments = Moment.objects.all()
    comments = []
    for _ in range(1000):
        date = Fake.date_between()
        comment = Comment(content=Fake.sentence(), user_id=User.objects.filter(id=random.randint(1, users.count()))[0],
                          moment_id=Moment.objects.filter(id=random.randint(1, moments.count()))[0],
                       pub_date=Fake.date_between_dates(date_start=date))
        comments.append(comment)
    Comment.objects.bulk_create(comments)



if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    application = get_wsgi_application()

    from app.models import Moment, User, Subscrition, Comment
    import random
    from faker import Faker

    main()
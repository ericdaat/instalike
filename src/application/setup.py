from .model import db, User, Post, Comments


def init_db():
    ###############
    # Init tables #
    ###############
    db.drop_all()
    db.create_all()

    #############
    # Add users #
    #############
    joe = User(
        username="joe",
        email="joe@example.com",
        fullname="Joe Awesome",
        bio="I'm Joe Awesome, humble yet awesome.",
        avatar="https://eu.ui-avatars.com/api/?size=300&name={0}".format("Joe+Awesome")
    )
    db.session.add(joe)
    db.session.commit()

    bob = User(
        username="bob",
        email="bob@example.com",
        fullname="Bob Awesome",
        bio="I'm Bob Awesome, humble yet awesome.",
        avatar="https://eu.ui-avatars.com/api/?size=300&name={0}".format("Bob+Awesome")
    )
    db.session.add(bob)
    db.session.commit()

    #############
    # Add posts #
    #############
    posts = [
        Post(
            user_id=joe.id,
            content="First post!",
            picture="https://picsum.photos/seed/seed1/600"
        ),
        Post(
            user_id=joe.id,
            content="Oh waow second post!",
            picture="https://picsum.photos/seed/seed2/600"
        ),
        Post(
            user_id=joe.id,
            content="I love this app so much",
            picture="https://picsum.photos/seed/seed3/600"
        ),
        Post(
            user_id=joe.id,
            content="Feeling like posting here",
            picture="https://picsum.photos/seed/seed4/600"
        ),
        Post(
            user_id=joe.id,
            content="Posting is fun",
            picture="https://picsum.photos/seed/seed5/600"
        ),
        Post(
            user_id=bob.id,
            content="First post for me!",
            picture="https://picsum.photos/seed/seed6/600"
        ),
    ]
    db.session.add_all(posts)
    db.session.commit()

    #############
    # Add likes #
    #############
    joe.likes.append(bob.posts[0])
    bob.likes.append(joe.posts[0])
    bob.likes.append(joe.posts[1])
    bob.likes.append(joe.posts[2])
    db.session.commit()

    ################
    # Add comments #
    ################
    joe.posts[0].comments.append(Comments(user=bob, content="great one!"))
    bob.posts[0].comments.append(Comments(user=joe, content="glad to see you here"))
    db.session.commit()

    ###############
    # Add follows #
    ###############
    joe.follows.append(bob)
    bob.follows.append(joe)
    db.session.commit()

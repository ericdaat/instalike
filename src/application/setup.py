import numpy as np

from .model import db, User, Post, Comments


def init_db(n_users=10, max_posts_per_user=10,
            max_likes_per_user=10, max_comments_per_user=10,
            max_follows_per_user=10):
    """ Initializes the database.
    Drop all the existing tables and create new ones.
    Then insert dummy data to get started with the application.
    """
    ###############
    # Init tables #
    ###############
    db.drop_all()
    db.create_all()

    #############
    # Read data #
    #############

    with open("data/names.txt") as f:
        data = f.readlines()

    firstnames = [line.strip() for line in data]

    #############
    # Add users #
    #############
    users = []

    for firstname in np.random.choice(firstnames, n_users):
        username = firstname.replace(" ", "_")

        u = User(
            username=username,
            email="{0}@example.com".format(username),
            fullname="{0} Awesome".format(username.title()),
            bio="Hi! I'm {0}.".format(firstname.title()),
            avatar="https://eu.ui-avatars.com/api/?size=300&name={0}+Awesome"\
                   .format(firstname.title())
        )

        users.append(u)

    db.session.add_all(users)
    db.session.commit()

    #############
    # Add posts #
    #############
    posts = []

    for user in users:
        for post_index in range(np.random.randint(0, max_posts_per_user)):
            p = Post(
                user_id=user.id,
                content="Post description.",
                picture="https://picsum.photos/seed/{0}-{1}/600"\
                        .format(user.username, str(post_index))
            )

            posts.append(p)

    db.session.add_all(posts)
    db.session.commit()

    #############
    # Add likes #
    #############
    for user in users:
        n_posts_to_like = np.random.randint(0, max_likes_per_user)

        for post in np.random.choice(posts, n_posts_to_like):
            user.likes.append(post)

    ################
    # Add comments #
    ################
    for user in users:
        n_posts_to_comment = np.random.randint(0, max_comments_per_user)

        for post in np.random.choice(posts, n_posts_to_comment):
            c = Comments(user=user, content="love it!")
            post.comments.append(c)

    ###############
    # Add follows #
    ###############
    for user_a in users:
        n_users_to_follow = np.random.randint(0, max_follows_per_user)

        for user_b in np.random.choice(users, n_users_to_follow):
            if user_a.username == user_b.username:
                continue

            user_a.follows.append(user_b)

    db.session.commit()

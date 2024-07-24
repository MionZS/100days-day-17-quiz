id_ = 0


class User:

    def __init__(self, username,  followers=0):
        global id_
        self.id_ = id_
        id_ += 1
        self.username = username
        self.followers = followers
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

    def list_user(self):
        print(self.username)
        print(self.id_)
        print(self.followers)
        print(self.following)
        print("-----------")


user_1 = User("waffle_rune")
user_2 = User("Lulu")

user_1.follow(user_2)
user_2.follow(user_1)

User.list_user(user_1)
User.list_user(user_2)

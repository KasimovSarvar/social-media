from os import remove

from django.test import TestCase
#
# posts = [
#     {'id': 1, 'image': 'file.png', 'author_id': 1},
#     {'id': 2, 'image': 'file.png', 'author_id': 2},
#     {'id': 3, 'image': 'file.png', 'author_id': 2},
#     {'id': 4, 'image': 'file.png', 'author_id': 2},
#     {'id': 5, 'image': 'file.png', 'author_id': 1},
#     {'id': 6, 'image': 'file.png', 'author_id': 3},
# ]
#
# comments = [
#     {'id': 1, 'message': 'text', 'post_id': 1, 'author_id': 1},
#     {'id': 2, 'message': 'text', 'post_id': 2, 'author_id': 1},
#     {'id': 3, 'message': 'text', 'post_id': 2, 'author_id': 1},
#     {'id': 4, 'message': 'text', 'post_id': 3, 'author_id': 1},
#     {'id': 5, 'message': 'text', 'post_id': 3, 'author_id': 1},
# ]
#
# # logic here
#
# _posts = [
#     {
#         'id': 1,
#         'image': 'file.png',
#         'author_id': 1,
#         'comments': [
#             {'id': 1, 'message': 'text', 'post_id': 1, 'author_id': 1}
#         ]
#     },
#     ...
#
# ]

# for key in posts:
#     for key1 in comments:
#         if key['id'] == key1['post_id']:
#             posts.append([key1])
#     print(posts)


# for post in posts:
#     post['comments'] = []
#     for comment in comments:
#         if post['id'] == comment['post_id']:
#             post['comments'].append(comment)
#
# print(posts)


# FOLLOW
# users = [
#     {'id': 1, 'username': 'user1'},
#     {'id': 2, 'username': 'user1'},
#     {'id': 3, 'username': 'user1'},
#     {'id': 4, 'username': 'user1'},
#     {'id': 5, 'username': 'user1'},
#     {'id': 6, 'username': 'user1'},
# ]
#
# follow_objects = [
#     {'follower': 1, 'following': 3},
#     {'follower': 1, 'following': 6},
#     {'follower': 2, 'following': 6},
#     {'follower': 3, 'following': 6},
# ]
#
# user_id = 1
#
# for user in users:
#     for follow in follow_objects:
#         if follow['following'] == user['id'] and follow['follower'] == user_id:
#             users.remove(user)
# print(users)

# FOLLOW
users = [
    {'id': 1, 'username': 'user1'},
    {'id': 2, 'username': 'user1'},
    {'id': 3, 'username': 'user1'},
    {'id': 4, 'username': 'user1'},
    {'id': 5, 'username': 'user1'},
    {'id': 6, 'username': 'user1'},
]

follow_objects = [
    {'follower': 1, 'following': 3},
    {'follower': 1, 'following': 6},
    {'follower': 2, 'following': 6},
    {'follower': 3, 'following': 6},
]

user_id = 2
filtered_users = []

for user in users:
    if user['id'] == user_id:
        continue
    append = True
    for follow in follow_objects:
        if follow['following'] == user['id'] and follow['follower'] == user_id:
            should_append = False
            break
    if append:
        filtered_users.append(user)

print(filtered_users)
































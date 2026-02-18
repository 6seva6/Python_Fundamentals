class Comment:
    def __init__(self, username, content, likes = 0):
        self.username = username
        self.content = content
        self.likes = likes

comment_1 = Comment('6seva6', 'social networks is evil', 3254235345)

print(comment_1.username)
print(comment_1.content)
print(comment_1.likes)
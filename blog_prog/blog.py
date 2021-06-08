from dataclasses import dataclass, field
from post import Post


@dataclass
class Blog:
    title: str
    author: str
    posts: list[Post] = field(default_factory=lambda: [])

    def __repr__(self) -> str:
        return f"{self.title} by {self.author} ({len(self.posts)} post{'s' if len(self.posts) > 1 else ''})"

    def create_post(self, title: str, content: str):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }

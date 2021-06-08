from dataclasses import dataclass

@dataclass
class Post:
    title: str
    content: str
    
    def json(self):
        return {
            "title": self.title,
            "content": self.content,
        }
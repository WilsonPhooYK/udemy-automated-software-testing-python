from unittest import TestCase, main
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))
        
    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('My Day', 'Rolf')
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (0 post)')
        
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Post', 'Post Content')
        
        b2 = Blog('My Day', 'Rolf')
        b2.create_post('Post', 'Post Content')
        b2.create_post('Post2', 'Post Content2')
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My Day by Rolf (2 posts)')
        
if __name__ == '__main__':
    main()

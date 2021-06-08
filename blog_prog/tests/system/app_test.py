from blog_prog.post import Post
from unittest import TestCase, main
from unittest.mock import patch
import app
from blog import Blog

class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
    
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'Test Create Blog', 'Test Author', 'q')
                
                app.menu()
                # Cannot call this if function is mocked since blog is never created
                # self.assertIsNotNone(app.blogs['Test Create Blog'])
                mocked_ask_create_blog.assert_called()
                
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)
            
    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()
            
            
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 post)')
            
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            # Creates a list of return values
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))
            
    def test_ask_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                
                mocked_print_posts.assert_called_with(app.blogs['Test'])
                
    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        blog.create_post('Test Post2', 'Test Content2')
        app.blogs = {'Test': blog}

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_any_call(blog.posts[0])
            mocked_print_post.assert_called_with(blog.posts[1])
            
    def test_print_post(self):
        post = Post('Test Post', 'Test Content')
        expected_print = '''
--- Test Post ---

Test Content
'''

        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)
            
    def test_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            # Creates a list of return values
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')
            app.ask_create_post()
            
            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Title')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')
        
if __name__ == "__main__":
    main()
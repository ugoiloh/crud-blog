from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice body content',
            author=self.user,
            )
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    def test_get_absolute_url(self):
       self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')
        
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'detail.html')

    def test_post_create_view(self): 
        response = self.client.post(reverse('blog:new_post'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id,
            })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.latest('date').title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')
        
    def test_post_update_view(self): 
        response = self.client.post(reverse('blog:edit_post', args='1'), {
        'title': 'Updated title',
        'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)
    
    def test_post_delete_view(self): 
        response = self.client.post(
        reverse('blog:delete_post', args='1'))
        self.assertEqual(response.status_code, 302)

    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    # def test_signup_form(self):
    #     new_user = get_user_model().objects.create_user(self.user)
    #     self.assertEqual(get_user_model().objects.all().count(), 1)
    #     self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        


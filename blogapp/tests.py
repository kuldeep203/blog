from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class PostModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title="Top 10 laptop",
            content="Asus 155lf.",
            author=self.user
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Top 10 laptop")
        self.assertEqual(self.post.content, "Asus 155lf.")
        self.assertEqual(self.post.author, self.user)
        self.assertTrue(self.post.published_date)

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/api/posts/")

        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/posts/1/")
        self.assertEqual(response.status_code, 200)


class CommentModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title="Top 10 laptop",
            content="Asus 155lf.",
            author=self.user
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            text="This is a test comment."
        )

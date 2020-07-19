
from django.forms import ModelForm
from .models import Blogs, Author

class BlogForm(ModelForm):
    class Meta:
        model = Blogs
        fields = ['author', 'blog_title', 'blog_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all()

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_name']
from django.urls import path
from .views import (index, blogs, blog_detail, blog_add, blog_update,
                    blog_delete, authors, author_add, author_update, author_delete)

urlpatterns = [
    path('', index),
    path('blogs', blogs),
    path('blogs/<int:blog_id>', blog_detail),
    path('blog/new', blog_add),
    path('blog/edit/<int:blog_id>', blog_update),
    path('blog/delete/<int:blog_id>', blog_delete),

    path('authors', authors),
    path('author/new', author_add),
    path('author/edit/<int:author_id>', author_update),
    path('author/delete/<int:author_id>', author_delete)
]
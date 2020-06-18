from django.urls import path
from .views import home, BlogDetailView, month_view, category_view, AddPost, user_posts_view, \
    user_created_blog, BlogUpdateView, user_created_blog_category_view, BlogDeleteView, user_created_blog_month_view

urlpatterns = [
    path('', home, name='blogs_home'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blogs/user/<str:username>/', user_posts_view, name='user_blogs'),
    path('blogs/created_blog/', user_created_blog, name='user_created_blog'),
    path('blogs/created_blog/category/<str:category>/', user_created_blog_category_view, name='user_created_blog_category'),
    path('blogs/created_blog/<str:month>/<int:year>/', user_created_blog_month_view, name='user_created_blog_month'),
    path('blogs/update_blog/<int:pk>/', BlogUpdateView.as_view(), name='user_update_blog'),
    path('blogs/delete_blog/<int:pk>/', BlogDeleteView.as_view(), name='user_delete_blog'),
    path('blogs/category/<str:category>/', category_view, name='blog_category'),
    path('blogs/<str:month>/<int:year>/', month_view, name='blog_month'),
    path('blogs/add-post/', AddPost.as_view(template_name='blogs/blog_form.html'), name='add_post'),
]

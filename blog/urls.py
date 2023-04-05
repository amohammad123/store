from django.contrib import admin
from django.urls import path
from blog import views as blog_view
from django.conf.urls.static import static
from basic_section.settings import DEBUG, MEDIA_ROOT, MEDIA_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',  blog_view.PostView.as_view()),
    path('posts/<int:post_id>/',  blog_view.PostView.as_view()),
    path('posts/<int:post_id>/like/',  blog_view.PostLikeView.as_view()),
    path('posts/<int:post_id>/comment/',  blog_view.CommentView.as_view()),
    path('posts/<int:post_id>/comment/<int:comment_id>/',  blog_view.CommentView.as_view()),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
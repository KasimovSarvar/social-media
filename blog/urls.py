from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.static import serve

from .views import home_view, signin_view, setting_view, signup_view, logout_view, like_view, \
    create_post_view, comment_view, create_prof_view, follow_view, delete_post_view, search_view

urlpatterns = [
    path('', home_view),
    path('setting/', setting_view),
    path('signin/', signin_view),
    path('signup/', signup_view),
    path('logout/', logout_view),
    path('like/', like_view),
    path('create/', create_post_view),
    path('comment/<int:pk>', comment_view),
    path('follow/', follow_view, name='follow_view'),
    path('profile/', create_prof_view),
    path('delete/<int:pk>', delete_post_view),
    path('search/', search_view),
    path('setting/', setting_view),
]


urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)
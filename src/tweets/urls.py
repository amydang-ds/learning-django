from django.urls import path


from .views import TweetDetailView, TweetListView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', TweetListView.as_view(), name='list'),
    path('<int:pk>', TweetDetailView.as_view(), name='detail'),
    # path('<int:pk>', tweet_detail_view, name='detail'),
] 

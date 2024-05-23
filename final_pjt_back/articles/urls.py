from django.urls import path
from . import views


urlpatterns = [
    path('community/', views.article_list),
    path('community/<int:article_pk>/', views.article_detail),
    path('community/<int:article_pk>/comments/', views.comment_list),
    path('community/<int:article_pk>/comments/<int:comment_pk>', views.comment_detail),
    path('qna/', views.qna_list),
    path('qna/<int:article_pk>/', views.qna_detail),
    path('qna/<int:article_pk>/comments/', views.qna_comment_list),
    path('qna/<int:article_pk>/comments/<int:comment_pk>', views.qna_comment_detail),

]

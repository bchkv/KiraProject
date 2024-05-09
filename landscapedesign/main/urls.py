from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # path('blog/', views.blog_home_1, name='blog_home_1'),
    # path('blog2/', views.blog_home_2, name='blog_home_2'),
    # path('post/', views.blog_post, name='blog_post'),
    path('contact/', views.contact, name='contact'),
    # path('faq/', views.faq, name='faq'),
    path('portfolio/1-col/', views.portfolio_1_col, name='portfolio_1_col'),
    # path('portfolio/2-col/', views.portfolio_2_col, name='portfolio_2_col'),
    # path('portfolio/3-col/', views.portfolio_3_col, name='portfolio_3_col'),
    # path('portfolio/4-col/', views.portfolio_4_col, name='portfolio_4_col'),
    # path('portfolio/item/', views.portfolio_item, name='portfolio_item'),
    # path('pricing/', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
]

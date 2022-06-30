from django.urls import path
from.views import index, about, blog, klass, contact, feature, single
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('class/', klass, name='klass'),
    path('contact/', contact, name='contact'),
    path('feature/', feature, name='feature'),
    path('single/', single, name='single'),
]
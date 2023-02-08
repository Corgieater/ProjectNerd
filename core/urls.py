from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('my_lists/', views.my_lists, name='my_lists'),
    path('accounts/', include('allauth.urls')),
    path('form/', views.form, name='form'),
    path('tag/<str:keyword>', views.get_exist_tag),
    # apis
    path('api/ce/list', views.CEListViews.as_view(), name='ce_list')
    # path('add_list/')
]

urlpatterns = urlpatterns+static(settings.STATIC_URL,
                                 document_root=settings.STATIC_ROOT)

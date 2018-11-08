from django.conf.urls import url

from .views import ( UpdateModelDetailAPIView,
                     UpdateModelListAPIView
                   )
urlpatterns = [
    url(r'^$', UpdateModelListAPIView.as_view()), #api/updates -> LIST/CREATE
    url(r'^(?P<id>\d+)/$', UpdateModelDetailAPIView.as_view()), #accetp digit
    #url(r'^$', json_view_view),
]

from django.conf.urls import url
from . import views


urlpatterns = (
    url(
        regex=r'^$',
        view=views.CheeseListView.as_view(),
        name='list'
    ),
)

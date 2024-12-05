from django.urls import path


from .views import custom_search


app_name = 'main'


urlpatterns = [
    path('suggest/', custom_search),
]

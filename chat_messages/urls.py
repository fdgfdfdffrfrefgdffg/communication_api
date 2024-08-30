from django.urls import path
from .views import AddOrGet, EditOrDel

urlpatterns = [
    path("", AddOrGet.as_view(), name="messages add"),
    path("<int:id>", EditOrDel.as_view(), name="messages get")
]
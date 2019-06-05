from django.urls import include, path
from api.views import ShowUsers, ListParking


urlpatterns = [
    path("", ShowUsers.as_view(), name="Show_Users"),
    path("parking/", ListParking.as_view(), name="List_Parking"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

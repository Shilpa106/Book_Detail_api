from django.urls import path
from .views import Record, Login, Logout,Record1, Login1, Logout1

urlpatterns = [
    path('addUser/', Record.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),


    # *********user
    path('addUser1/', Record1.as_view(), name="register"),
    path('login1/', Login1.as_view(), name="login"),
    path('logout1/', Logout1.as_view(), name="logout"),
]

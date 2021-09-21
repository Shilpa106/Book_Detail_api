from django.urls import path
from .views import BookRecord
# , Login, Logout,Record1, Login1, Logout1

urlpatterns = [
    path('addBook/', BookRecord.as_view(), name="record"),
    
]


from django.urls import path
from .views import admin_home, admin_item, admin_category, admin_attribute

app_name = "store"

urlpatterns = [
    path('admin/',admin_home,name ="admin_home"),
    path('admin-item/',admin_item,name ="admin_item"),
    path('admin-category/',admin_category,name ="admin_category"),
    path('admin-attribute/',admin_attribute,name ="admin_attribute")
]
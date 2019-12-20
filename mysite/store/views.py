from django.shortcuts import render

# Create your views here.

def admin_home(request):
    context ={}
    context["active_link"] = "admin_home"
    context["menu_title"] = "home"
    return render(request,"admin_home.html",context)

def admin_item(request):
    context ={}
    context["active_link"] = "admin_item"
    context["menu_title"] = "Item"
    return render(request,"admin_items_list.html",context)

def admin_category(request):
    context ={}
    context["active_link"] = "admin_category"
    context["menu_title"] = "Category"
    return render(request,"admin_items_list.html",context)

def admin_attribute(request):
    context ={}
    context["active_link"] = "admin_attribute"
    context["menu_title"] = "Attribute"
    return render(request,"admin_items_list.html",context)
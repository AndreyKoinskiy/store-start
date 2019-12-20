from django.contrib import admin
from django.db.models import Q
from .models import (
                        Category, Item,
                        Attribute, Unit,
                        ImageItem, AttributeCategory,
                        AttributeItemValue
)
# Register your models here.
class ItemInline(admin.TabularInline):
    model = Item

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2
        if obj:
            return Category.objects.count()
        return extra
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

admin.site.register(Category, CategoryAdmin)

class AttributeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Attribute, AttributeAdmin)

class UnitAdmin(admin.ModelAdmin):
    pass

admin.site.register(Unit, UnitAdmin)

class ImageItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImageItem, ImageItemAdmin)

class AttributeCategoryAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent__isnull = False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    pass

admin.site.register(AttributeCategory, AttributeCategoryAdmin)

class AttributeItemValueInline(admin.TabularInline):
    model = AttributeItemValue

    def get_extra(self, request, obj=None, **kwargs):
        extra = 2
        if obj:
            return Category.objects.count()
        return extra

class AttributeItemValueAdmin(admin.ModelAdmin):
    pass

admin.site.register(AttributeItemValue, AttributeItemValueAdmin)

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        AttributeItemValueInline,
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(parent__isnull = False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            # hide MyInline in the add view
            print(inline)
            if not isinstance(inline, AttributeItemValueInline) or obj is not None:
                 yield inline.get_formset(request, obj), inline

admin.site.register(Item, ItemAdmin)
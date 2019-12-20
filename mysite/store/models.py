from django.db import models
from django.utils.timezone import now
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_pub = models.BooleanField(default=False)
    slug = models.SlugField()
    parent = models.ForeignKey('self',on_delete = models.PROTECT, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_pub = models.BooleanField(default=False)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits=2,decimal_places=2)
    category = models.ForeignKey('Category', related_name='categories', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Attribute(models.Model):
    name = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_pub = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class ImageItem(models.Model):
    picture = models.ImageField()
    item = models.ForeignKey('Item',on_delete=models.CASCADE)
    def __str__(self):
        return self.item.name + " picture"

    def __unicode__(self):
        return self.item.name + " picture"

class AttributeCategory(models.Model):
    attribute = models.ForeignKey("Attribute", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + " -> " + self.attribute.name

    def __unicode__(self):
        return self.category.name + " -> " + self.attribute.name
        

class AttributeItemValue(models.Model):
    attribute = models.ForeignKey('Attribute',on_delete=models.CASCADE)
    item = models.ForeignKey('Item',on_delete=models.CASCADE)
    numerical_value = models.DecimalField(max_digits=2,decimal_places=2)
    text_value = models.CharField(max_length = 255)
    unit = models.ForeignKey('Unit',on_delete=models.PROTECT)

    def __str__(self):
        return self.item.name + " -> " + self.attribute.name + " -> Value"


    def __unicode__(self):
        return self.item.name + " -> " + self.attribute.name + " -> Value"

from django.contrib import admin
from mrango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'url')
	

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
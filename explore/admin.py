from django.contrib import admin
from .models import Post

#tell django about our plans rofl
class adminpage(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, adminpage)

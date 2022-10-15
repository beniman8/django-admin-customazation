from django.contrib import admin
from . import forms
from . import models


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    site_title = 'Blog Admin Area'
    site_title = 'Site Blog Admin Area'


blog_site = BlogAdminArea(name='BlogAdmin')





class PostAdmin(admin.ModelAdmin):
    form = forms.PostForm
    fieldsets = (
        ('Section 1', {
            "fields": (
                'title','author',           
            ),
            "description":'This is the description of this thing',
        }),

         ('Section 2', {
            "fields": (
                'slug',    
            ),
            'classes':(
                'collapse',
            )
        }),
    )
    


blog_site.register(models.posts,PostAdmin)

# admin.site.register(models.Post)
# admin.site.register(models.Category)
# admin.site.register(models.posts)  Normally we do this



#cusomize what is in youe admin panel if you want only certain things available for people to see
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title','author']

admin.site.register(models.Post,PostAdmin)


#another way to do the samething is to @admin.register on top of the class 
# @admin.register(models.Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title','author']


#this her is to register all the models from all your apps
# import django.apps  

# models = django.apps.apps.get_models()


# for model in models:

#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass

# #This here is to rmove the stuff you do not like from your backend if you use  a for loop 
# admin.site.unregister(django.contrib.sessions.models.Session)
# [
# <class 'django.contrib.admin.models.LogEntry'>,
# <class 'django.contrib.auth.models.Permission'>,
# <class 'django.contrib.auth.models.Group'>,
# <class 'django.contrib.auth.models.User'>,
# <class 'django.contrib.contenttypes.models.ContentType'>,
# <class 'django.contrib.sessions.models.Session'>,
# <class 'blog.models.posts'>, 
# <class 'blog.models.Category'>, 
# <class 'blog.models.Post'>""
# ]


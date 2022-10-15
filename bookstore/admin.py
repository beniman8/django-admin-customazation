from django.contrib import admin


class BookstoreAdminArea(admin.AdminSite):
    site_header = 'BookStore Admin Area'
    site_title = 'BookStore Admin Area'
    site_title = 'Site BookStore Admin Area'


bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')




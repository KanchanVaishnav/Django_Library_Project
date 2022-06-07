from django.contrib import admin

from enroll.models import Book
class BookAdmin(admin.ModelAdmin):
    list_display=['name','isbn','author','category']
admin.site.register(Book,BookAdmin)

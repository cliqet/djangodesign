from django.contrib import admin
from .models import Blog, Category
import csv
from django.http import HttpResponse


# this class will be used to export queryset for different models as CSV
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = 'Export as CSV'


class BlogAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ('title', 'content', 'category', 'post_date', 'author')
    ordering = ['post_date']
    actions = ['export_as_csv']
    list_display = ('id', 'title', 'post_date', 'username', 'blog_author')
    list_display_links = ['title']
    list_per_page = 20
    search_fields = ['title']


class CategoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ('name',)
    ordering = ['name']
    actions = ['name']
    list_display = ('id', 'name')
    list_display_links = ['name']
    list_per_page = 5
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)




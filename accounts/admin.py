from django.contrib import admin
from .models import AuthorProfile
import csv
from django.http import HttpResponse
from django.utils.safestring import mark_safe


THUMBNAIL_WIDTH = 100
THUMBNAIL_HEIGHT = 100

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


class AuthorProfileAdmin(admin.ModelAdmin, ExportCsvMixin):
    fields = ('headshot', 'image',  'author', ('date_of_birth', 'gender',), 'address', 'contact_number')
    readonly_fields = ['headshot', ]
    ordering = ['author__last_name']
    actions = ['export_as_csv']
    list_display = ('id', 'username', 'last_name', 'first_name', 'gender', 'contact_number')
    list_filter = ('gender',)
    list_display_links = ['username']
    list_per_page = 20
    search_fields = ['author__last_name', 'author__first_name']

    def headshot(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height="{height}" />'.format(
            url=obj.image.url,
            width=THUMBNAIL_WIDTH,
            height=THUMBNAIL_HEIGHT,
        )
    )


admin.site.register(AuthorProfile, AuthorProfileAdmin)

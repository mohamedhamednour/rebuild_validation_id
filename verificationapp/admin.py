from django.contrib import admin

# Register your models here.


from .models import MiddelwareRequestID

@admin.register(MiddelwareRequestID)
class MiddelwareRequestIDAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'path', 'method', 'status_code', 'created_at')
    search_fields = ('request_id', 'path', 'method')
    list_filter = ('status_code',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
import csv
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.models import User

def export_users_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    writer.writerow(['Username', 'Email'])
    for user in queryset:
        writer.writerow([user.username, user.email])
    return response

export_users_csv.short_description = "Export Selected Users to CSV"

class UserAdmin(admin.ModelAdmin):
    actions = [export_users_csv]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

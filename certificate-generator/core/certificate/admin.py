from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Certificate


admin.site.site_header = "Adventure Sports Club Admin"
admin.site.site_title = "Adventure Sports Club Admin Portal"
admin.site.index_title = "Welcome to Adventure Sports Club Certificate Portal"

# Register your models here.
# class CertificateAdminConfig(UserAdmin):
#     # form = UserChangeForm
#     # add_form = UserCreationForm
#     model = Certificate
    
#     search_fields = ('name','gender','event')
#     list_filter = ('gender','event','hours','kilometers','top_effort',)
#     ordering = ('event',)
#     # list_display = ('name','gender','event','hours','kilometers','top_effort',)
#     fieldsets = (
#         ('ParticipantCredentials', {'fields' : ('name','gender','event')}),
#         ('Performance', {'fields' : ('hours','kilometers','top_effort',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes' : ('wide',),
#             'fields' : ('name','gender','event','hours','kilometers','top_effort',),
#         }),
#     )
#     # filter_horizontal = ()
    
# admin.site.register(Certificate,CertificateAdminConfig)

admin.site.register(Certificate)
from django.contrib.admin.apps import AdminConfig

class WebsiteAdminConfig(AdminConfig):
    default_site = 'base.admin.WebsiteAdminSite'
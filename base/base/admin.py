from django.contrib import admin

class WebsiteAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Menues": 1,
            "Entrees": 2,
            "First_dishes": 3,
            "Second_dishes": 4,
            "Side_dishes": 5,
            "Desserts": 6,
            "Wines": 7,
            "Opening_hours": 8,
            "Contacts": 9,
            "Gallery_images": 10,
            "Groups":11,
            "Users":12,
        }
        app_dict = self._build_app_dict(request)
        
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        

        #Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list
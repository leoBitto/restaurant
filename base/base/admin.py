from django.contrib import admin

class WebsiteAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        ordering = {
            "Menues": 1,
            "Business_Menues": 2,
            "Entrees": 3,
            "First_dishes": 4,
            "Second_dishes": 5,
            "Side_dishes": 6,
            "Desserts": 7,
            "Wines": 8,
            "Opening_hours": 9,
            "Contacts": 10,
            "Gallery_images": 11,
            "Groups":12,
            "Users":13,
        }
        app_dict = self._build_app_dict(request)
        
        # a.sort(key=lambda x: b.index(x[0]))
        # Sort the apps alphabetically.
        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
        

        #Sort the models alphabetically within each app.
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])

        return app_list
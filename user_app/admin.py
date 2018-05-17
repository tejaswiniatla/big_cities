from django.contrib import admin
from user_app.models import City,Organization,User,Article,Tag,Tagged_article

admin.site.register(City)
admin.site.register(Organization)
admin.site.register(User)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Tagged_article)

# Register your models here.

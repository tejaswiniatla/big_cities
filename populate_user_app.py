import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','big_cities.settings')

import django
django.setup()

#fake pop Script

import random
from user_app.models import City,Organization,User,Article,Tag,Tagged_article

from faker import Faker

fakegen = Faker('en_US')
# city = ['Chicago', 'Atlanta', 'New York', 'Detroit', 'Virginia']

# def add_city():
#     # Commented out line 19 as that is the old method attempted for creating a fake city model
#     # c = city.objects.get_or_create(city_name=random.choice(city))[0]
#     c = City.objects.get_or_create(city_name=fake.city, city_description=fake.paragraph)[0]
#     c.save()
#
#
#     return c

def populate(N=5):

    for entry in range(N):
        # Line 30 may not be necessary as the add_city funciton is not relevant
        # newcity = add_city()

        fake_city_name = fakegen.city_name()
        fake_city_description = fakegen.city_description()
        fake_org_name = fakegen.org_name()
        fake_org_address = fakegen.org_address()
        fake_user_name = fakegen.name()
        fake_user_email= fakegen.email()
        fake_user_phone= fakegen.phone()
        fake_art_title= fakegen.art_title()
        fake_art_description = fakegen.art_description ()
        fake_url = fakegen.url()
        fake_tag_keyword= fakegen.tag_keyword()

        newcity = City.objects.get_or_create(city_name=fake_city_name, city_description=fake_city_description)[0]

        neworg = Organization.objects.get_or_create(city=newcity,org_name=fake_org_name,org_address=fake_org_address)[0]

        newuser = User.objects.get_or_create(org=neworg,user_name=fake_user_name,user_email=fake_user_email,user_phone=fake_user_phone)[0]

        newarticle = Article.objects.get_or_create(user=newuser,art_title=fake_art_title,art_description=fake_art_description,url=fake_url)[0]

        newtag = Tag.objects.get_or_create(tag_keyword=fake_tag_keyword)[0]

    if __org_name__ == '__main__':
        print("populating script!")
        populate(20)
        print("populating complete!")

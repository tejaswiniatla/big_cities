from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=30)
    city_description = models.CharField(max_length=500)

    def __str__(self):
        return self.city_name

class Organization(models.Model):
    org_name = models.CharField(max_length=50)
    org_address = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.org_name

class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50)
    user_phone = models.IntegerField()
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

class Article(models.Model):
    art_title = models.CharField(max_length=250)
    art_description = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.art_title

class Tag(models.Model):
    tag_keyword = models.CharField(max_length=50)
    #articles = models.ManyToManyField(Article)

class Tagged_article(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    

from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Content(models.Model):
    type = models.CharField(max_length=50)
    content = models.TextField()
    site_id = models.ForeignKey('Site', on_delete=models.CASCADE)
    page_id = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def from_page_type(self, foreign_id):
        return self.type == Page.objects.get(page_id=foreign_id)

    def from_page_content(self, foreign_id):
        return self.type == Page.objects.get(page_id=foreign_id)

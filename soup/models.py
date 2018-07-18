from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Content(models.Model):
    type = models.CharField(max_length=50)
    site = models.ForeignKey('Site', on_delete=models.CASCADE)
    page = models.ForeignKey('Page', on_delete=models.CASCADE)

    def __str__(self):
        return self.type

    def from_page_type(self, foreign_id):
        return self.type == Page.objects.get(page_id=foreign_id)

    def from_page_content(self, foreign_id):
        return self.type == Page.objects.get(page_id=foreign_id)


class ContentLine(models.Model):
    content_line = models.TextField()
    content_type = models.CharField(max_length=3)
    content = models.ForeignKey('Content', on_delete=models.CASCADE)
    line_number = models.IntegerField()

    def __str__(self):
        return self.content_line

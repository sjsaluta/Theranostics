from time import strptime
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

class Assessment(models.Model):
    name = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Assessment", kwargs={"slug": self.slug})

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class BoneMetastasis(models.Model):
    name = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class screeningLesions(models.Model):
    name = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class ptLesions(models.Model):
    name = models.CharField(max_length=300,null=True, unique=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class fuLesions(models.Model):
    name = models.CharField(max_length=300,null=True, unique=True)
    college = models.ForeignKey(College,on_delete=models.CASCADE,null=True)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Patients(models.Model):
    name = models.CharField(max_length=300, null=True, unique=True)
    slug = models.SlugField(null=True)
    assessment = models.ForeignKey(Assessment,on_delete=models.CASCADE,null=True)
    bonemeta = models.ForeignKey(BoneMetastasis,on_delete=models.CASCADE,null=True)
    s_lesions = models.ForeignKey(screeningLesions,on_delete=models.CASCADE,null=True)
    side_effect = models.BooleanField()
    pt_lesions = models.ForeignKey(ptLesions, on_delete=models.CASCADE, null=True)
    pt_number = models.IntegerField()
    fu_lesions = models.ForeignKey(fuLesions, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    #auto-add slugs
    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
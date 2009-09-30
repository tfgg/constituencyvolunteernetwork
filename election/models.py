from django.db import models

from signup.models import Constituency

from slugify import smart_slugify

class Party(models.Model):
    class Meta:
        verbose_name_plural="Parties"

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=80)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("/election/parties/%s" % self.slug)

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = smart_slugify(self.name)
        super(Party, self).save(*args, **kwargs)


class Candidate(models.Model):
    """
    A Candidate stands in a Constituency, possibly reprisenting a Party.
    """
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    party = models.ForeignKey(Party)
    constituency = models.ForeignKey(Constituency)
    email = models.EmailField(blank=True)
    address = models.TextField(max_length=300, blank=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return ("/election/candidates/%s" % self.slug)
    
    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = smart_slugify(self.name)
        super(Candidate, self).save(*args, **kwargs)

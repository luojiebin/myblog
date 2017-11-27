import collections
from operator import attrgetter

from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(publish=True)

    def recent_posts(self, number):
        return self.get_queryset().all()[:number]

    def year_carchive(self):
        dd = collections.defaultdict(list)
        for post in self.get_queryset():
            dd[post.created.year].append(post)
        return [(year, dd[year]) for year in sorted(dd)]


class TagManager(models.Manager):
    def ordered_by_capacity(self):
        tags = self.get_queryset()
        return sorted(list(tags), key=attrgetter('capacity'), reverse=True)


class Tag(TimeStampedModel):
    name = models.CharField(max_length=16, unique=True)
    slug = models.SlugField()

    objects = TagManager()

    @property
    def capacity(self):
        return self.post_set.count()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:tag_detail', args=[self.slug])

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField()
    content = models.TextField()
    publish = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, blank=True)

    objects = models.Manager()
    published = PublishedPostManager()

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.slug])

    def __str__(self):
        return 'Post<{}>'.format(self.title)


class About(models.Model):
    content = models.TextField(verbose_name='About myself')

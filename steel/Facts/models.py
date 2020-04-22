from django.db import models
from  django.contrib.auth.models import User
from django.db.models import Count
from  django.shortcuts import reverse
# Create your models here.
from django.utils.text import slugify


class LinkManager(models.Manager):
    def get_queryset(self):
            return super(LinkManager, self).get_queryset().annotate(
                vote=Count('voters')).order_by("-vote")


class Link(models.Model):
    title=models.CharField("HeadLines",max_length=100,unique=True)
    submitter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    submitted_on=models.DateTimeField(auto_now_add=True)
    rank_score=models.FloatField(default=0.0)
    url=models.URLField("URL",max_length=250,blank=True)
    description= models.TextField(blank=True)
    with_votes=LinkManager()
    objects=models.Manager()
    slug=models.SlugField(blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        super(Link, self).save(*args, **kwargs)

    def get_absolute_voteurl(self):
        return reverse('vote',kwargs={'slug':self.slug})

    def get_absolute_linkdetail(self):
        return reverse('linkdetail',kwargs={'slug':self.slug})


class Voters(models.Model):
    link=models.ForeignKey(Link,on_delete=models.CASCADE,null=True)
    voter=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE,null=True)
    bio=models.TextField(blank=True)
    # def save(self,*args,**kwargs):
    #     self.bio=slugify("hi "+self.user)
    #     super(UserProfile,self).save(*args,**kwargs)



def createProfile(sender,instance,created,**kwargs):
    if created:
        profile,created=UserProfile.objects.get_or_created(user=instance)


from django.db.models.signals import post_save
post_save.connect(createProfile,sender=User)



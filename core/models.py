from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

class Places(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    general_price = models.FloatField(null=True)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class InterestsActivities(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_('Full Name'), max_length=25)
    email = models.EmailField(_('Email Address'), unique=True)
    is_applicant = models.BooleanField(_('Applicant'), default=False)
    is_admin = models.BooleanField(_('Admin'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)
    isGuide = models.BooleanField(default=False)
    places_of_interest = models.ManyToManyField(Places, related_name='user_places_of_interest')
    interests = models.ManyToManyField(InterestsActivities, related_name='InterestsActivities')
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def clean(self):
        super().clean() 
        self.email = self.__class__.objects.normalize_email(self.email)
# class CustomUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     isGuide = models.BooleanField(default=False)
#     places_of_interest = models.ManyToManyField(Places, related_name='user_places_of_interest')
#     interests = models.ManyToManyField(InterestsActivities, related_name='InterestsActivities')

class Hiring(models.Model):
    traveller = models.ForeignKey(CustomUser, related_name='hiring_traveller', on_delete=models.SET_NULL, null=True)
    guide = models.ForeignKey(CustomUser, related_name='hiring_guide', on_delete=models.SET_NULL, null=True)
    place = models.ForeignKey(Places, related_name='hiring_place', on_delete=models.SET_NULL, null=True)
    pay = models.FloatField(null=True)
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractBaseUser
from AHApps.master.models import TimestampModel
from AHApps.master.utils.UNIQUE.generate_password import create_password
from AHApps.master.utils.UNIQUE.generate_primary_key import create_primary_key
import os
import uuid

class Artist(TimestampModel):
    artist_id = models.CharField(primary_key=True, max_length=255, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    mobile = models.CharField(max_length=255, unique=True, null=False, blank=False)
    password = models.CharField(max_length=255, blank=True)
    otp = models.CharField(max_length=255, default='545663')
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.artist_id:
            last_artist_id = Artist.objects.all().order_by('-created_at').first()
            if last_artist_id:
                new_artist_id = "AH000" + str(int(str(last_artist_id.artist_id)[5:]) + 1)
            else:
                new_artist_id = "AH0001"

            self.artist_id = new_artist_id

        if not self.password:
            self.password = create_password()

        if self.is_active:
            subject = "Welcome to Artist Hub! Your Login Credentials Inside"
            message = f"""
            Welcome to Our Platform, {self.artist_id}!

            Thank you for joining us. Here are your login credentials:
            Artist ID: { self.artist_id }
            Password: { self.password }
            We recommend changing your password after logging in for the first time.

            Best regards,
            The Team Artist Hub 
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [f'{self.email}']
            send_mail(subject, message, from_email, recipient_list)

        super(Artist, self).save(*args, **kwargs)
        # Create ArtistProfile if not exists
        if not hasattr(self, 'artistprofile'):
            ArtistProfile.objects.get_or_create(artist_id=self)


class ArtistProfile(TimestampModel):
    GENDER_CHOICES = (
        ('male', "Male"),
        ('female', "Female"),
        ('other', "Other"),
    )
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    profile = models.ImageField(default="default-images/artist-profile.png")
    first_name = models.CharField(max_length=255, default='-', blank=True, null=True)
    last_name = models.CharField(max_length=255, default='-', blank=True, null=True)
    gender = models.CharField(max_length=255, default="other", choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address=models.CharField(max_length=255, default="-", blank=True, null=True)
    
    def save(self, *args, **kwargs):
        # Fetch the current object from the database to compare
        try:
            existing_profile = ArtistProfile.objects.get(pk=self.pk)
        except ArtistProfile.DoesNotExist:
            existing_profile = None

        # Only update the image name if a new image is uploaded
        if self.profile and (not existing_profile or existing_profile.profile != self.profile):
            if self.profile.name.startswith('default-images'):
                new_filename = self.profile.name
                self.profile.name = os.path.join(new_filename)
            else:
                base, ext = os.path.splitext(self.profile.name)
                new_filename = f"{self.artist_id.artist_id}_profile{ext}"
                self.profile.name = os.path.join('artist_profiles/', new_filename)
        
        super(ArtistProfile, self).save(*args, **kwargs)


class ArtistCatalogueCategory(TimestampModel):
    name = models.CharField(max_length=255, blank=False, null=False)
    

    def __str__(self):
        return self.name

class ArtistCatalogue(TimestampModel):
    POST_FIX = 'catalogue'
    artist_catalogue_id = models.CharField(primary_key=True, blank=True, max_length=255)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ArtistCatalogueCategory, related_name='catalogues')
    catalogue_image = models.ImageField(default="default-images/default-catalogue-image.png")
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.artist_id}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.artist_catalogue_id = create_primary_key(self.POST_FIX)

        if self.catalogue_image:
            if self.catalogue_image.name.startswith('default-images'):
                new_filename = self.catalogue_image.name
                self.catalogue_image.name = os.path.join(new_filename)
            else:
                base, ext = os.path.splitext(self.catalogue_image.name)
                new_filename = f"{self.artist_catalogue_id}_image{ext}"
                self.catalogue_image.name = os.path.join('artist_catalogue_images/', new_filename)
        super(ArtistCatalogue, self).save(*args, **kwargs)


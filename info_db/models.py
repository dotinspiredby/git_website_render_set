from django.db import models


class BioLang(models.Model):
    language_id = models.CharField(max_length=20)
    text = models.TextField()
    objects = models.Manager()

    
class RepertoirePieceOrchestra(models.Model):
    composer = models.CharField(max_length=100)
    title = models.TextField()
    objects = models.Manager()


class RepertoirePieceWPiano(models.Model):
    composer = models.CharField(max_length=100)
    title = models.TextField()
    objects = models.Manager()


class RepertoirePieceSolo(models.Model):
    composer = models.CharField(max_length=100)
    title = models.TextField()
    objects = models.Manager()


class RepertoirePieceChamber(models.Model):
    composer = models.CharField(max_length=100)
    title = models.TextField()
    objects = models.Manager()


class ContactInfo(models.Model):
    contact_person = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.IntegerField(blank=True)
    objects = models.Manager()


class ContactInfoNoAddress(models.Model):
    contact_person = models.CharField(max_length=200)
    telephone = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, blank=True)
    e_mail = models.EmailField()
    e_mail_optional = models.EmailField(blank=True)
    objects = models.Manager()


class PhotoFileLink(models.Model):
    # file = models.ImageField(upload_to='photos/')
    # For GoogleDrive links (slow)
    description = models.CharField(max_length=400)
    link = models.CharField(max_length=500)
    objects = models.Manager()


class PhotoFile(models.Model):
    file = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=400)
    objects = models.Manager()


class VideoLink(models.Model):
    description = models.TextField()
    link = models.TextField()
    objects = models.Manager()


class Publication(models.Model):
    title = models.CharField(max_length=400)
    date = models.DateField()
    photo_preview = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    link = models.TextField()
    objects = models.Manager()

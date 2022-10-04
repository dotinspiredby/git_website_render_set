from django.contrib import admin
from .models import BioLang, ContactInfo, ContactInfoNoAddress, PhotoFile, PhotoFileLink, VideoLink, \
    RepertoirePieceSolo, RepertoirePieceWPiano, RepertoirePieceOrchestra, \
    RepertoirePieceChamber, Publication

admin.site.register(BioLang)
admin.site.register(ContactInfo)
admin.site.register(ContactInfoNoAddress)
admin.site.register(PhotoFile)
admin.site.register(PhotoFileLink)
admin.site.register(VideoLink)
admin.site.register(RepertoirePieceSolo)
admin.site.register(RepertoirePieceWPiano)
admin.site.register(RepertoirePieceOrchestra)
admin.site.register(RepertoirePieceChamber)
admin.site.register(Publication)

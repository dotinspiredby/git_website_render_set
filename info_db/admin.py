from django.contrib import admin
from .models import BioLang, ContactInfo, ContactInfoNoAddress, PhotoFile, VideoLink, \
    RepertoirePieceSolo, RepertoirePieceWPiano, RepertoirePieceOrchestra, RepertoirePieceChamber
# from .models import BioDE, BioEN, BioRU


admin.site.register(BioLang)
# admin.site.register(BioEN)
# admin.site.register(BioDE)
# admin.site.register(BioRU)
admin.site.register(ContactInfo)
admin.site.register(ContactInfoNoAddress)
admin.site.register(PhotoFile)
admin.site.register(VideoLink)
admin.site.register(RepertoirePieceSolo)
admin.site.register(RepertoirePieceWPiano)
admin.site.register(RepertoirePieceOrchestra)
admin.site.register(RepertoirePieceChamber)

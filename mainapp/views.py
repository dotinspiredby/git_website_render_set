from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.views import View
from .forms import FeedbackForm
from portfolio.settings import EMAIL_HOST_USER, RECIPIENTS_EMAIL
# from info_db.models import BioDE, BioEN, BioRU
from info_db.models import BioLang, ContactInfo, ContactInfoNoAddress, PhotoFile, PhotoFileLink, VideoLink, \
    RepertoirePieceSolo, RepertoirePieceWPiano, RepertoirePieceOrchestra, RepertoirePieceChamber, Publication
from django.core.exceptions import ObjectDoesNotExist
from event_db.models import EventModel
import json


class PageManager(View):
    def get(self, request):
        return render(request, 'main_page.html')

    def get_bio(self, request):
        language_id = str(request.path).split('/')[-1]
        bios = BioLang.objects.all()
        try:
            bio = BioLang.objects.get(language_id__iexact=language_id)
        except ObjectDoesNotExist:
            bio = BioLang.objects.get(pk=1)
            return redirect(f"/{bio.language_id}/")

        return render(request, "bio_page.html", context={'bios': bios,
                                                         'sel_bio': bio})

    def get_repertoire(self, request):
        solo = RepertoirePieceSolo.objects.order_by('composer')
        piano = RepertoirePieceWPiano.objects.order_by('composer')
        orchestra = RepertoirePieceOrchestra.objects.order_by('composer')
        chamber = RepertoirePieceChamber.objects.order_by('composer')
        return render(request, 'repertoire.html', context={'solo_rep': solo,
                                                           'piano_rep': piano,
                                                           'orch_rep': orchestra,
                                                           'chamber_rep': chamber})

    def get_events(self, request):
        events = EventModel.objects.order_by('-date')
        return render(request, 'event_page.html', context={'events': events})

    def get_media(self, request):
        photos = PhotoFile.objects.all()
        photo_links = PhotoFileLink.objects.all()
        videos = VideoLink.objects.all()
        return render(request, 'presskit_page.html', context={'presskit': photo_links,
                                                              'pics': photos,
                                                              'videos': videos})

    def get_contacts(self, request):
        contacts = ContactInfo.objects.all()
        press_contacts = ContactInfoNoAddress.objects.all()
        return render(request, 'contact_page.html', context={'contacts': contacts, 'press_contacts': press_contacts})

    def get_feedback_page(self, request):
        return render(request, 'feedback_page.html')

    def feedback(self, request):
        if request.method == 'GET':
            form = FeedbackForm()
        elif request.method == 'POST':
            form = FeedbackForm(request.POST)
            if form.is_valid():
                message_file = json.dumps({
                    'from': form.cleaned_data['address'],
                    'subject': form.cleaned_data['subject'],
                    'text': form.cleaned_data['text']
                })
                # address = form.cleaned_data['address']
                # subject = form.cleaned_data['subject']
                # text = form.cleaned_data['text']
                try:
                    send_mail("Inquiry from Website", message_file, EMAIL_HOST_USER, RECIPIENTS_EMAIL)
                except BadHeaderError:
                    return HttpResponse('Error in subject')
                return render(request, 'feedback_success.html')
            else:
                return HttpResponse('Wrong request')
        return render(request, "feedback_page.html")

    def get_publications(self, request):
        publications = Publication.objects.order_by('-date')
        return render(request, "publications.html", context={'publications': publications})


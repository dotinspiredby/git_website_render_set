from django import forms


class FeedbackForm(forms.Form):
    address = forms.EmailField(label="E-mail", required=True)
    subject = forms.CharField(label='Subject', required=True)
    text = forms.CharField(label='Message', widget=forms.Textarea, required=True)

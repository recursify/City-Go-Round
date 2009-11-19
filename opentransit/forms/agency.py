from django import forms

class AgencyForm(forms.Form):
    name            = forms.CharField()
    gtfs_data_exchange_id     = forms.CharField(required=False)
    short_name      = forms.CharField(required=False)
    city            = forms.CharField(required=False)
    state           = forms.CharField(max_length=2,required=False)
    country         = forms.CharField(required=False)
    postal_code     = forms.IntegerField(required=False)
    address         = forms.CharField(required=False)
    agency_url      = forms.URLField(required=False)
    executive       = forms.CharField(required=False)
    executive_email = forms.EmailField(required=False)
    twitter         = forms.CharField(required=False)
    contact_email   = forms.EmailField(required=False)
    updated         = forms.DateTimeField(required=False)
    phone           = forms.CharField(required=False)

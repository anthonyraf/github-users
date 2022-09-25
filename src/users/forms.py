from django import forms
from . import github_api as github_api

COUNTRIES = tuple(
    (n, country) for (n, country) in zip(range(1,len(github_api.COUNTRIES_JSON.values())+1), github_api.COUNTRIES_JSON.values())
)
print(COUNTRIES)

class SearchForm(forms.Form):
    countries = forms.ChoiceField(choices=COUNTRIES, label="", widget=forms.Select(attrs={"class":"col form-select mt-3"})) 
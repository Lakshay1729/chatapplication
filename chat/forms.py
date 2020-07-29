from django import forms


class username(forms.Form):
    room_name=forms.CharField()
    user_name=forms.CharField()
from django_unicorn.components import UnicornView
from django.shortcuts import redirect


class EmailView(UnicornView):
    email = ""

    def register_email(self):
        return redirect('/register')

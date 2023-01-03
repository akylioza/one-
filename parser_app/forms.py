from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOISES = (
        ('FILMS', "FILMS"),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'FILMS':
            film_parser = parser.parser()
            for i in film_parser:
                models.FilmParser.objects.create(**i)
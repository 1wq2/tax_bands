import os
import sys

import django

INIT_TAXES = [
    {
        'begin': 0,
        'end': 12_500,
        'percent': 0,
    },
    {
        'begin': 12_501,
        'end': 50_000,
        'percent': 20,
    },
    {
        'begin': 50_001,
        'end': 150_000,
        'percent': 40,
    },
    {
        'begin': 150_001,
        'end': None,
        'percent': 45,
    },
]


def init_db():
    from taxes.models import Tax

    Tax.objects.all().delete()

    for tax in INIT_TAXES:
        Tax.objects.create(**tax)


if __name__ == '__main__':
    sys.path.append(os.path.abspath(os.path.dirname(__file__)))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'tax_bands.settings')
    django.setup()

    init_db()

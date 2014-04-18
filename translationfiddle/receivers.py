from django.dispatch import receiver
from django.utils.translation.trans_real import translation
from django.utils.translation.trans_real import _translations
from startupsignal import startup


@receiver(startup)
def reload_translations(sender, **kwargs):
    """Reload the translations.
    """
    for language in _translations:
        del _translations[language]
        translation(language)

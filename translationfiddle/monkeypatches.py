from django.utils.translation.trans_real import DjangoTranslation

from .signals import translation_fiddle


def merge(self, other):
    """Merge two message catalogs.
    """
    self._catalog.update(other._catalog)

    # send signal translation_fiddle
    translation_fiddle.send(sender=self, other=other)

# patch method merge of class DjangoTranslation
DjangoTranslation.merge = merge

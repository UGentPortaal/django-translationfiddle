django-translationfiddle
========================

Runtime modifications to message catalogs.


USAGE
-----

1. Add ``django-translationfiddle`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...

        'translationfiddle',

        ...
    )

2. Create a receiver for signal ``translation_fiddle``, that modifies the
   translation object (argument ``sender``).  Argument ``other`` is the message
   catalog that was just added to the translation object::

    from django.dispatch import receiver
    from translationfiddle import translation_fiddle

    @receiver(translation_fiddle)
    def modify_messages(sender, **kwargs):
        # modify english translations
        if sender.language().startswith("en"):

            # get the other message catalog
            other = kwargs["other"]

            # check info about the other message catalog
            info = other._info

            # modify the message catalog
            sender._catalog["foo"] = "Foo!"


CONTRIBUTORS
------------

- Bert Vanderbauwhede <bert.vanderbauwhede@ugent.be>

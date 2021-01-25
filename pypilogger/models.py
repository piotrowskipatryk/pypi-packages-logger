from django.db import models
from django.utils.translation import ugettext_lazy as _

class Package(models.Model):
    """ Package model - for keeping PyPI packages info """
    title = models.CharField(_("title"), max_length=255)
    link = models.CharField(_("link"), max_length=255)
    guid = models.CharField(_("guid"), max_length=255)
    description = models.TextField(_("description"), null=True, blank=True)
    author = models.CharField(_("author"), max_length=255, null=True, blank=True)
    author_email = models.CharField(_("author email"), max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField(_("publication date"))
    keywords = models.TextField(_("keywords"), null=True, blank=True)
    version = models.CharField(_("version"), max_length=50)
    # -- maintainer details --
    maintainer = models.CharField(_("maintainer"), max_length=50, null=True, blank=True)
    maintainer_email = models.CharField(_("mainteiner email"), max_length=50, null=True, blank=True)

    def __str__(self):
        return self.title

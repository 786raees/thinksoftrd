from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CompanyInfo(models.Model):

    name = models.CharField(_("Company Name"), max_length=100, default='ThinkSoftRD')
    logo_light = models.ImageField(_("Logo Light"), upload_to='uploads', default='logo.jfif')
    logo_dark = models.ImageField(_("Logo Dark"), upload_to='uploads', default='logo.jfif')
    favicon = models.ImageField(_("Favicon"), upload_to='uploads', default='logo.jfif')
    email = models.EmailField(_("E-Mail"), max_length=254)
    phone = models.CharField(_("Phone Number"), max_length=100, default='+92 315-0040764')
    address = models.TextField(_("Address"), default='Khan House, Kot Ali Garh, Kasur')

    class Meta:
        verbose_name = _("Company info")
        verbose_name_plural = _("Company Info")

    def __str__(self):
        return self.name

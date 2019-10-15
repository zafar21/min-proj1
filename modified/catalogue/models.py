from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    pass 

from oscar.apps.catalogue.models import *
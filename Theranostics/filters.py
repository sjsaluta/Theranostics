import django_filters
import json

from .models import *


#Filtering the rooms
class PatientsFilter(django_filters.FilterSet):

    capacity = django_filters.RangeFilter()

    class Meta:
        model = Patients
        fields = ('assessment','bonemeta','s_lesions','side_effect', 'pt_lesions', 'pt_number', 'fu_lesions')
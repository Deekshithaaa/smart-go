from django import forms
from .models import Dt

class DtForm(forms.ModelForm):
    class Meta:
        model= Dt
        fields= ["days","same_dest","par",'dist','sechom','ty_sechom','of_sechom','rea_sechom','adv_plan','fam_hol','worries','njoy','pet','high_cost','mul_dest','reas','trans','influ','us','tim_shr','c1','c2','c3','c4','p1','p2','p3','p4']

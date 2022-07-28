from multiprocessing import context
from django.shortcuts import render
from FamilyApp.models import Family
def family_members(request):
    family_context={
        "members": Family.objects.all()
    }
    return render(request, "template.html", context=family_context)
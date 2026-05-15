from rest_framework import viewsets
from apps.contacts.models import Contact
from apps.contacts.serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.select_related('student').all()
    serializer_class = ContactSerializer
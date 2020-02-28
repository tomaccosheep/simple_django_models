import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
from contacts.models import Contact

while True:
    print('\n'.join([contact.name for contact in Contact.objects.all()]))
    Contact(name=input("New person's name: ")).save()

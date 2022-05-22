from djchoices import DjangoChoices, ChoiceItem

class AddressType(DjangoChoices):
    Residential = ChoiceItem('residential')
    Office = ChoiceItem('office')

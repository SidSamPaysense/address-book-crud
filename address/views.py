import http

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from address.models import AddressEntry
from address.serializers import AddressEntrySerializer


class AddressEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows addresses to be created, viewed, edited or deleted

    Creating an address entry involves passing the user's email and phone as well.
    If you pass an existing phone or email, we will link the existing user to the new address.
    Both the phone and email (if available) are used to check the existence of a user.
    If it's a new phone and email, we will create a new user and link it to the new address.

    NOTE: Deletion does NOT involve hard deletion from the database
    Only a boolean flag is set to False to denote deletion, and such addresses are filtered out in the GET call

    Any "deleted"/inactive addresses are NOT retrieved in the GET call
    """

    serializer_class = AddressEntrySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AddressEntry.objects.active().by_user(self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        address = self.get_object()
        address.mark_inactive()
        address.save()
        return Response(status=http.HTTPStatus.NO_CONTENT)




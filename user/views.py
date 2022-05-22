import http

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response

from user.models import AddressBookUser
from user.serializers import AddressBookUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be created, viewed, edited or deleted
    You can only operate on the users that you created
    Any users created by others will not be viewable to you

    NOTE: Deletion does NOT involve hard deletion from the database
    Only a boolean flag is set to False to denote deletion, and such users are filtered out in the GET call

    Any "deleted"/inactive addresses are NOT retrieved in the GET call
    """

    serializer_class = AddressBookUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AddressBookUser.objects.active().by_user(self.request.user.id)

    def destroy(self, request, *args, **kwargs):
        address = self.get_object()
        address.mark_inactive()
        address.save()
        return Response(status=http.HTTPStatus.NO_CONTENT)




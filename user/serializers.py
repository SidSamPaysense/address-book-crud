from rest_framework import serializers

from user.models import AddressBookUser


class AddressBookUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['added_by'] = self.context['request'].user
        return super().create(validated_data)


    class Meta:
        model = AddressBookUser
        exclude = ('added_by', 'is_active')

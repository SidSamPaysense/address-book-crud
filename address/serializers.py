from rest_framework import serializers

from address.models import AddressEntry
from user.models import AddressBookUser
from user.serializers import AddressBookUserSerializer


class AddressEntrySerializer(serializers.ModelSerializer):
    user = AddressBookUserSerializer(read_only=True)

    # the following fields are for a possible new user
    first_name = serializers.CharField(max_length=20, write_only=True)
    last_name = serializers.CharField(max_length=20, allow_null=True, allow_blank=True, write_only=True)
    phone = serializers.CharField(max_length=15, allow_null=True, allow_blank=True, write_only=True)
    email = serializers.EmailField(allow_null=True, allow_blank=True, write_only=True)

    def validate(self, attrs):
        first_name = attrs.get('first_name')
        last_name = attrs.get('last_name')
        phone = attrs.get('phone')
        email = attrs.get('email')

        ser = AddressBookUserSerializer(data={
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        })
        ser.is_valid(raise_exception=True)
        return attrs

    def _fetch_existing_user(self, phone, email):
        if phone and email:
            kwargs = {'phone': phone, 'email': email}
        elif phone:
            kwargs = {'phone': phone}
        elif email:
            kwargs = {'email': email}
        else:
            kwargs = {}

        if kwargs:
            user_obj = AddressBookUser.objects.active().filter(**kwargs).first()
        else:
            user_obj = None

        return user_obj

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name', '')
        phone = validated_data.pop('phone', '')
        email = validated_data.pop('email', '')

        user_obj = self._fetch_existing_user(phone, email)

        if not user_obj:
            create_kwargs = {
                'first_name': first_name,
                'last_name': last_name,
                'phone': phone,
                'email': email,
                'added_by': self.context['request'].user
            }
            user_obj = AddressBookUser.objects.create(**create_kwargs)

        validated_data['user'] = user_obj
        validated_data['added_by'] = self.context['request'].user
        return super().create(validated_data)

    class Meta:
        model = AddressEntry
        exclude = ('is_active', 'added_by')

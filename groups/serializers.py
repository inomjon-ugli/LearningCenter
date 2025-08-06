from rest_framework import serializers
from .models import Group

class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'group_name',
            'course',
            'teacher',
            'start_date',
            'end_date',
            'schedule',
            'is_active',
        )
        read_only_fields = ['id',]
        extra_kwargs = {
            'group_name':{'required':True}
            
        }
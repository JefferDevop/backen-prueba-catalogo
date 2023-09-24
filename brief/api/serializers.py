from rest_framework import serializers
from brief.models import Brief


class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = ['id', 'usuario', ]

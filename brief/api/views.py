from rest_framework.viewsets import ModelViewSet

from brief.models import Brief
from brief.api.serializers import BriefSerializer


class BriefApiViewSet(ModelViewSet):
    serializer_class = BriefSerializer
    queryset = Brief.objects.all()




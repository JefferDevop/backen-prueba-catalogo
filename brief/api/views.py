from rest_framework.viewsets import ModelViewSet

from accounts.models import Brief
from accounts.api.serializers import BriefSerializer


class BriefApiViewSet(ModelViewSet):
    serializer_class = BriefSerializer
    queryset = Brief.objects.all()




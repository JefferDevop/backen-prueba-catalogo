from rest_framework.routers import DefaultRouter


from brief.api.views import BriefApiViewSet

router_brief = DefaultRouter()

router_brief.register(
    prefix='brief', basename='brief', viewset=BriefApiViewSet)


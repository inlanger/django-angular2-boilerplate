from django.conf.urls import url, include
from dummy.models import Person
from rest_framework import routers, serializers, viewsets

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name')

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

router = routers.DefaultRouter()
router.register(r'users', PersonViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

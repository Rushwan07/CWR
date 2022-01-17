from rest_framework.authentication import SessionAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import MessagesAreaSerilizer
from .models import MessagesArea

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class MessagesAreaModelViewSet(ModelViewSet):
    queryset = MessagesArea.objects.all().order_by('timeStamp')
    serializer_class = MessagesAreaSerilizer
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')
    authentication_classes = (CsrfExemptSessionAuthentication, )

    def list(self, request, *args, **kwargs):
        current_chats = self.request.query_params.get('current_chats', None)
        if current_chats:
            self.queryset = MessagesArea.objects.all()[::-1][int(current_chats): int(current_chats)+5]
        else:
            self.queryset = {}
        return super(MessagesAreaModelViewSet, self).list(request, *args, **kwargs)

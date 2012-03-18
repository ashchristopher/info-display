from django.views.generic import TemplateView

from display.models import SubscriberCount
from display.mixins import JSONResponseMixin


class HomeView(TemplateView):

    template_name = 'display/home.html'

    def get(self, request):
        try:
            subscribers = SubscriberCount.objects.latest('date_added')
        except SubscriberCount.DoesNotExist:
            subscribers = None
 
        context = {
            'total_subscribers' : getattr(subscribers, 'total_subscribers', 'No Data')
        }
 
        return self.render_to_response(context)


class JSONView(JSONResponseMixin, HomeView):
    
    template_name = None

from django.views.generic import TemplateView

from display.models import SubscriberCount, YesterdaysSignupsCount
from display.mixins import JSONResponseMixin


NO_DATA = 'No Data'

class HomeView(TemplateView):

    template_name = 'display/home.html'

    def get(self, request):
        try:
            subscribers = SubscriberCount.objects.latest('date_added')
        except SubscriberCount.DoesNotExist:
            subscribers = None

        try:
            yesterdays_signups = YesterdaysSignupsCount.objects.latest('date_added')
        except YesterdaysSignupsCount.DoesNotExist:
            yesterdays_signups = None
 
        context = {
            'total_subscribers' : getattr(subscribers, 'total_subscribers', NO_DATA),
            'yesterdays_signups' : getattr(yesterdays_signups, 'subscribers', NO_DATA),
        }
 
        return self.render_to_response(context)


class JSONView(JSONResponseMixin, HomeView):
    
    template_name = None

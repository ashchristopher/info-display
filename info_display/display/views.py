from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from display.models import SubscriberCount, YesterdaysSignupsCount
from display.mixins import JSONResponseMixin


NO_DATA = 'No Data'

class HomeView(TemplateView):

    template_name = 'display/home.html'


    def get_context_data(self):
        """ Get the context with subscriber info populated. """
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

        return context

    def get(self, request):

        # only let staff accounts view the data.
        if not request.user.is_staff:
            context = {
                'total_subscribers' : '--',
                'yesterdays_signups' : '--',
            }
        else:
            context = self.get_context_data()

        return self.render_to_response(context)


class JSONView(JSONResponseMixin, HomeView):
    
    template_name = None

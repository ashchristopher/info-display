import locale

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from display.models import SubscriberCount, YesterdaysSignupsCount
from display.mixins import JSONResponseMixin


NO_DATA = 'No Data'

class HomeView(TemplateView):

    template_name = 'display/home.html'

    def get(self, request):

        # initialize the context
        context = {
            'total_subscribers' : '--',
            'yesterdays_signups' : '--',
            'total_subscribers_raw' : '--',
            'yesterdays_signups_raw' : '--',
        }


        # only let staff accounts view the data.
        if request.user.is_staff:
            locale.setlocale(locale.LC_ALL, 'en_US')

            try:
                subscribers = SubscriberCount.objects.latest('date_added')
                context['total_subscribers_raw'] = subscribers.total_subscribers
                context['total_subscribers'] = locale.format("%d", subscribers.total_subscribers, grouping=True)
            except SubscriberCount.DoesNotExist:
                pass

            try:
                yesterdays_signups = YesterdaysSignupsCount.objects.latest('date_added')
                context['yesterdays_signups_raw'] = yesterdays_signups.subscribers
                context['yesterdays_signups'] = locale.format("%d", yesterdays_signups.subscribers, grouping=True)
            except YesterdaysSignupsCount.DoesNotExist:
                pass

        return self.render_to_response(context)


class JSONView(JSONResponseMixin, HomeView):
    
    template_name = None

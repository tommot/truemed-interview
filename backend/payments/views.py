import json

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

stripe.api_key = settings.STRIPE_SECRET_KEY


@require_http_methods(["POST"])
@csrf_exempt
def charge_view(request):
    try:
        truemed_payment_session_redirect_url = 'https://bing.com'
        # Create a Truemed PaymentSession here

        return HttpResponse({
            json.dumps({"redirect_url": truemed_payment_session_redirect_url})
        })
    # Something else happened, completely unrelated to Stripe
    except Exception as e:
        return HttpResponse(
            json.dumps({"message": "Unable to process payment, try again."})
        )

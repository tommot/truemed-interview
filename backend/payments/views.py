import json
import requests

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

stripe.api_key = settings.STRIPE_SECRET_KEY

TRUE_MED_PAYMENT_ENDPOINT = (
    f"{settings.TRUE_MED_API_BASE}/payments/v1/create_payment_session"
)


@require_http_methods(["POST"])
@csrf_exempt
def charge_view(request):
    try:
        # Parse the amount and currency from the form data
        amount = int(request.POST.get("amount"))
        # currency = request.POST.get("currency")
        customer_name = request.POST.get("customer_name")
        idempotency_key = request.POST.get("idempotency_key")
        cart_items_json = request.POST.get("cart_items_json")
        cart_items = json.loads(cart_items_json)
        order_items = []
        for cart_item in cart_items:
            order_items.append(
                {
                    "name": cart_item["name"],
                    "amount": int(100 * float(cart_item["price"])),
                    "quantity": cart_item["quantity"],
                    "sku": cart_item["id"],
                }
            )

        # Create a Truemed PaymentSession here
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-truemed-api-key": settings.TRUE_MED_API_KEY,
        }
        data = {
            "total_amount": amount,
            "idempotency_key": idempotency_key,
            "success_url": "http://localhost:3000/checkout?paymentStatus=success",
            "failure_url": "http://localhost:3000/checkout?paymentStatus=failure",
            "order_items": order_items,
            "customer_name": customer_name,
            "customer_email": "placeholder@placeholder.com",
        }

        response = requests.post(TRUE_MED_PAYMENT_ENDPOINT, headers=headers, json=data)
        response_data = response.json()
        redirect_url = response_data.get("redirect_url")
        return HttpResponse({json.dumps({"redirect_url": redirect_url})})
    # Something else happened, completely unrelated to Stripe
    except Exception as e:
        return HttpResponse(
            json.dumps({"message": "Unable to process payment, try again."})
        )

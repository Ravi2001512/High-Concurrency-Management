from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product


@api_view(["POST"])
def purchase(request):

    product_id = request.data.get("product_id")

    if not product_id:
        return Response(
            {"error": "product_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        with transaction.atomic():

            product = Product.objects.select_for_update().get(
                id=product_id
            )

            if product.stock <= 0:
                return Response(
                    {"message": "Out of stock"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            product.stock -= 1
            product.save()

            remaining_stock = product.stock

        return Response(
            {
                "message": "Purchase successful",
                "remaining_stock": remaining_stock
            },
            status=status.HTTP_200_OK
        )

    except Product.DoesNotExist:
        return Response(
            {"error": "Product not found"},
            status=status.HTTP_404_NOT_FOUND
        )
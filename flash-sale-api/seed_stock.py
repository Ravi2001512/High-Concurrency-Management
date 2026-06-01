import os
import sys


def setup_django():
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

    import django
    django.setup()


def seed_stock(product_id=1, stock=50, name="Keyboard"):
    setup_django()

    from products.models import Product

    product, created = Product.objects.update_or_create(
        id=product_id,
        defaults={"name": name, "stock": stock},
    )
    return product, created


if __name__ == "__main__":
    product, created = seed_stock()
    print(
        f"product_id={product.id} name='{product.name}' stock={product.stock} created={created}"
    )

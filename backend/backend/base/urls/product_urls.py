from django.urls import path
from base.views import product_views as views


urlpatterns = [
    path("", views.getProducts, name="products"),
    path("farm-products/", views.getFarmProducts, name="products"),
    path("animal-products/", views.getAnimalProducts, name="products"),
    path("highest-points/", views.getFilteredProductHighestPoints, name="products"),
    path("highest-price/", views.getFilteredProductHighestPrice, name="products"),
    path("lowest-price/", views.getFilteredProductLowestPrice, name="products"),
    path(
        "points_4_5_and_higher/",
        views.getFilteredProductWithPoints4_5AndHigher,
        name="products",
    ),
    path(
        "points_4/",
        views.getFilteredProductWithPoints4,
        name="products",
    ),
    path(
        "points_3_5_and_higher/",
        views.getFilteredProductWithPoints3_5AndHigher,
        name="products",
    ),
    path(
        "points_3/",
        views.getFilteredProductWithPoints3,
        name="products",
    ),
    path("<str:pk>/", views.getProduct, name="product"),
]

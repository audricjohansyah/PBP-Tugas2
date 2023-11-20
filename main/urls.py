from django.urls import path
from main.views import create_product_flutter, show_main
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, delete_product, decrement_amount, increment_amount, add_product_ajax, get_product_json, catalogue_view, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete-product/<int:id>/', delete_product, name='delete_product'),
    path('increment-amount/<int:id>/', increment_amount, name='increment_amount'),
    path('decrement-amount/<int:id>/', decrement_amount, name='decrement_amount'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('catalogue-view/', catalogue_view, name='catalogue_view'),
    path('delete-product-ajax/<int:id>/', delete_product_ajax, name='delete_product_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
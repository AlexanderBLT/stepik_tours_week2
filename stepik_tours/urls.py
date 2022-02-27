from django.urls import path
from stepik_tours.error_handlers import custom_handler400, custom_handler403, custom_handler404, custom_handler500
import tours.views


urlpatterns = [
    path('', tours.views.main_view, name='main'),
    path('departure/<str:departure_from>', tours.views.departure_view, name='departure'),
    path('tour/<int:tour_id>', tours.views.tour_view, name='tour')
    ]

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500

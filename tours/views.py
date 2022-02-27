from django.shortcuts import render
from django.http import HttpResponseNotFound
from random import sample
import tours.data as data


def main_view(request):
    tours = dict(sample(data.tours.items(), 6))

    return render(request, 'tours/index.html', context={
                                                        'title': data.title,
                                                        'subtitle': data.subtitle,
                                                        'tours': tours,
                                                        'description': data.description
                                                        })


def departure_view(request, departure_from):
    departure = data.departures.get(departure_from)
    if departure_from not in data.departures:
        return HttpResponseNotFound('<h1>Такой страницы не существует!</h1>')

    tours = data.tours.copy()
    for tour_id, value in list(tours.items()):
        if tours[tour_id]['departure'] != departure_from:
            del tours[tour_id]
    minimum_price = min([tours[tour]['price'] for tour in tours])
    maximum_price = max([tours[tour]['price'] for tour in tours])
    minimum_nights = min([tours[tour]['nights'] for tour in tours])
    maximum_nights = max([tours[tour]['nights'] for tour in tours])

    return render(request, 'tours/departure.html', context={
                                                            'departure': departure,
                                                            'tours': tours,
                                                            'minimum_nights': minimum_nights,
                                                            'maximum_nights': maximum_nights,
                                                            'minimum_price': minimum_price,
                                                            'maximum_price': maximum_price
                                                            })


def tour_view(request, tour_id):
    if tour_id not in data.tours:
        return HttpResponseNotFound('<h1>Такой страницы не существует!</h1>')

    tour = data.tours.get(tour_id).copy()
    tour['departure'] = data.departures[tour['departure']]

    return render(request, 'tours/tour.html', context={'tour': tour})

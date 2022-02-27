import tours.data


def departures(request) -> dict:
    departures = tours.data.departures
    return {'departures': departures}

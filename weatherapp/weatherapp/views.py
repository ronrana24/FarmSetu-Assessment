from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect
from .services import ClimateDataFetcher
from . import constant

def index(request: HttpRequest) -> JsonResponse:
    """
    Returns a JSON response with a list of available regions and parameters.

    :param request: The HTTP request object.
    :return: A JsonResponse containing available parameters, regions, and endpoints.
    """
    return JsonResponse({
        "message": "List of all regions and parameters",
        "parameter": constant.PARAMETERS,
        "region": constant.REGIONS,
        "available_endpoints": [
            "http://127.0.0.1:8000/",
            "http://127.0.0.1:8000/dataset/--Parameter--/weather/--Region--/",
            "http://127.0.0.1:8000/healthcheck/",
        ]
    })

def get_healthcheck(request: HttpRequest) -> JsonResponse:
    """
    Returns a health check response to indicate the service is running.

    :param request: The HTTP request object.
    :return: A JsonResponse indicating the service status.
    """
    return JsonResponse({
        "message": "All Good!",
    })

def get_dataset(request: HttpRequest, parameter: str, region: str) -> JsonResponse:
    """
    Fetches climate data for a specified parameter and region.

    :param request: The HTTP request object.
    :param parameter: The climate parameter to fetch.
    :param region: The geographical region for which to fetch the data.
    :return: A JsonResponse containing the fetched data or an error message if not found.
    """
    fetcher = ClimateDataFetcher(parameter, region)
    data = fetcher.fetch_data()
    
    if data is None:
        # Return an error message if data is not found
        return JsonResponse({
            "message": "Data not found. Use the below parameters and regions.",
            "parameters": constant.PARAMETERS,
            "regions": constant.REGIONS
        })
    
    return JsonResponse(data=data)

def custom_404(request: HttpRequest) -> JsonResponse:
    """
    Redirects to the home page for any unmatched routes.

    :param request: The HTTP request object.
    :return: A redirect response to the home page.
    """
    return redirect("/")
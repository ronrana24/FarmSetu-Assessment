from django.http import JsonResponse, HttpRequest
from typing import Any

from django.shortcuts import redirect

from .services import ClimateDataFetcher
from . import constant

def index(request: HttpRequest) -> JsonResponse:
    return JsonResponse({
        "message": "List of all regions and parameters",
        "parameter": constant.PARAMETERS,
        "region": constant.REGIONS,
        "available end-points": [
            "http://127.0.0.1:8000/",
            "http://127.0.0.1:8000/dataset/--Parameter--/weather/--Region--/",
            "http://127.0.0.1:8000/healthcheck/",
        ]
    })

def get_healthcheck(request: HttpRequest) -> JsonResponse:
    return JsonResponse({
        "message": "All Good!",
    })

def get_dataset(request: HttpRequest, parameter: str, region: str) -> JsonResponse:
    fetcher = ClimateDataFetcher(parameter, region)
    data = fetcher.fetch_data()
    
    if data is None:
        return JsonResponse({"message": "Data not found"})
    return JsonResponse(data=data)
    
def custom_404(request: HttpRequest):
    return redirect("/")

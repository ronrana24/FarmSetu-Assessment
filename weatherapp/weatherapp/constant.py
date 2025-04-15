DOMAIN = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"

def create_region_data(region_name):
    return {
        "MaxTemp": f"{DOMAIN}Tmax/ranked/{region_name}.txt",
        "MinTemp": f"{DOMAIN}Tmin/ranked/{region_name}.txt",
        "MeanTemp": f"{DOMAIN}Tmean/ranked/{region_name}.txt",
        "Sunshine": f"{DOMAIN}Sunshine/ranked/{region_name}.txt",
        "Rainfall": f"{DOMAIN}Rainfall/ranked/{region_name}.txt",
        "Raindays": f"{DOMAIN}Raindays1mm/ranked/{region_name}.txt",
        "DaysOfAirfrost": f"{DOMAIN}AirFrost/ranked/{region_name}.txt"
    }

DATA = {
    "UK": create_region_data("UK"),
    "England": create_region_data("England"),
    "Wales": create_region_data("Wales"),
    "Scotland": create_region_data("Scotland"),
    "Northern Ireland": create_region_data("Northern_Ireland"),
    "England & Wales": create_region_data("England_and_Wales"),
}

REGIONS = ["UK", "England", "Wales", "Scotland", "Northern Ireland", "England & Wales"]
PARAMETERS = ["MaxTemp", "MinTemp", "MeanTemp", "Sunshine", "Rainfall", "Raindays", "DaysOfAirfrost"]
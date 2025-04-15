DOMAIN = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"

def create_region_data(region_name):
    return {
        "Max Temp": f"{DOMAIN}Tmax/ranked/{region_name}.txt",
        "Min Temp": f"{DOMAIN}Tmin/ranked/{region_name}.txt",
        "Mean Temp": f"{DOMAIN}Tmean/ranked/{region_name}.txt",
        "Sunshine": f"{DOMAIN}Sunshine/ranked/{region_name}.txt",
        "Rainfall": f"{DOMAIN}Rainfall/ranked/{region_name}.txt",
        "Raindays ≥1.0mm": f"{DOMAIN}Raindays1mm/ranked/{region_name}.txt",
        "Days of Air frost": f"{DOMAIN}AirFrost/ranked/{region_name}.txt"
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
PARAMETERS = ["Max Temp", "Min Temp", "Mean Temp", "Sunshine", "Rainfall", "Raindays ≥1.0mm", "Days of Air frost"]
import requests
from constant import DATA

class ClimateDataFetcher:
    def __init__(self, parameter, region):
        self.parameter = parameter
        self.region = region
        self.parsed_data = []
        
    def _get_url(self) -> str:
        return DATA.get(self.region, {}).get(self.parameter, '')

    def fetch_data(self):
        # Fetch the content of the file
        URL = self._get_url()
        if (len(URL) == 0):
            return None
        
        response = requests.get(URL)
        data = response.text

        # Split the data into lines
        lines = data.splitlines()

        # Assuming the first line contains headers
        message = "\n".join(lines[:4])
        last_updated = " ".join(lines[4].split()[2:])
        
        headings = lines[5].strip().split("   ") # -> Heading
        parsed_values = []

        for line, index in lines[6:]:
            parsed_line = line.strip().split("   ")
            parsed_values.append(parsed_line)
            print(index)
            
        print(parsed_values)
        # Rest data
        # print(lines[6].strip().split("   "))
        
        return self._format_response(message=message, last_updated=last_updated)
        
    def _format_response(self, message: str, last_updated: str):
        return {
            "message": message,
            "last_updated": last_updated
        }
        
    def _get_data_into_json(headers: list[str], values: list[str]):
        parsed_data = []
        for header, value in zip(headers, values):
            # Split the value into the actual value and the year
            temp_value, year = value.split()
            # Create a dictionary for the current entry
            entry = {
                "month_or_season": header.strip(),
                "value": float(temp_value),
                "year": int(year)
            }
            parsed_data.append(entry)
            
        return parsed_data
    
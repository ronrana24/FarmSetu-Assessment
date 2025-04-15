import requests
from .constant import DATA

class ClimateDataFetcher:
    def __init__(self, parameter: str, region: str):
        """
        Initializes the ClimateDataFetcher with a specific parameter and region.

        :param parameter: The climate parameter to fetch (e.g., temperature, precipitation).
        :param region: The geographical region for which to fetch the data.
        """
        self.parameter = parameter
        self.region = region
        self.parsed_data = {}

    def _get_url(self) -> str:
        """
        Retrieves the URL for the specified parameter and region from the DATA constant.

        :return: The URL as a string, or an empty string if not found.
        """
        return DATA.get(self.region, {}).get(self.parameter, '')

    def fetch_data(self):
        """
        Fetches climate data from the specified URL, processes it, and stores it in a structured format.

        :return: A dictionary containing a message, last updated timestamp, and parsed data, or None if URL is invalid.
        """
        URL = self._get_url()
        if not URL:  # Check if the URL is valid
            return None
        
        response = requests.get(URL)
        data = response.text

        # Split the data into lines
        lines = data.splitlines()

        # Extract the message and last updated timestamp
        message = "\n".join(lines[:4])
        last_updated = " ".join(lines[4].split()[2:])

        # Extract headings from the data
        headings = lines[5].strip().split("   ")

        # Process each line of data
        for line in lines[6:-1]:
            parsed_line = line.strip().split("   ")
            
            for index, entry in enumerate(parsed_line):
                data, year = entry.strip().split("  ")
                month_data = headings[index].strip().split("  ")[0]
                self.append_data(data, year, month_data)
        
        return self._format_response(message=message, last_updated=last_updated)

    def append_data(self, data: str, year: str, month: str):
        """
        Appends the fetched data to the parsed_data dictionary.

        :param data: The climate data value.
        :param year: The year associated with the data.
        :param month: The month or season associated with the data.
        """
        if year not in self.parsed_data:
            self.parsed_data[year] = {}
        
        # Store the data for the specific month
        self.parsed_data[year][month] = data

    def _format_response(self, message: str, last_updated: str):
        """
        Formats the response to be returned after data fetching.

        :param message: A message containing information about the data.
        :param last_updated: The last updated timestamp of the data.
        :return: A dictionary containing the formatted response.
        """
        return {
            "message": message,
            "last_updated": last_updated,
            "data": self.parsed_data
        }

    @staticmethod
    def _get_data_into_json(headers: list[str], values: list[str]):
        """
        Converts the headers and values into a structured JSON-like format.

        :param headers: A list of headers (e.g., months or seasons).
        :param values: A list of corresponding values with years.
        :return: A list of dictionaries containing structured data.
        """
        parsed_data = []
        for header, value in zip(headers, values):
            temp_value, year = value.split()
            entry = {
                "month_or_season": header.strip(),
                "value": float(temp_value),
                "year": int(year)
            }
            parsed_data.append(entry)
        
        return parsed_data
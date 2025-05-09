# Constants
import json
from backend.custom_tools.tool import Tool
import googlemaps

from backend.network import make_request_post

API_KEY = "AIzaSyAC1c_yUCOj-UpfK6ReYzDmS42HuR6Gwb8"  # Replace with your actual API key

class SalvationTool(Tool):
    def __init__(self):
        super().__init__(name="salvation_tool",
                         description="A tool that gets nearby Salvation Army Locations given a location. Find Salvation Army locations that provide disaster relief. Use this when the user asks for Salvation Army. It will return an with a field results, which is an array of json objects representing the salvation army locations, where displayName is an HTML string containing the name, googleMapsUri is the URL for the salvation army location, and adrFormatAddress is the address",
                         properties={
							"latitude": {
								"type": "number",
								"description":" The latitude of the requested location"
							},
							"longitude": {
								"type": "number",
								"description": "The longitude of the requested location"
							}
                         })

    async def tool_call(self, latitude: float, longitude: float):
        salvation_army = await make_request_post("https://places.googleapis.com/v1/places:searchText", headers={
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": "places.displayName,places.googleMapsUri,places.adrFormatAddress"
        }, data={
            "textQuery": "Salvation Army",
        })

        print(salvation_army)
        # fire_stations = gmaps.places(query=query, location={
        #     "lat": latitude,
        #     "lng": longitude
        #     }, radius=5000)
        # 
        # print(fire_stations)
        # fire_stations = await nearby_text_search(latitude, longitude, 5000, query)
        
        if salvation_army:
            return json.dumps(salvation_army)
        return "Something Went Wrong."

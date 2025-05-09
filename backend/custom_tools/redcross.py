# Constants
import json
from backend.custom_tools.tool import Tool
import googlemaps

from backend.network import make_request_post

API_KEY = "AIzaSyAC1c_yUCOj-UpfK6ReYzDmS42HuR6Gwb8"  # Replace with your actual API key

class RedCrossTool(Tool):
    def __init__(self):
        super().__init__(name="red_cross_tool",
                         description="A tool that gets nearby Red Cross Locations given a location. Use this when the user asks for Red Cross. It will return an with a field results, which is an array of json objects representing the red cross locations, where displayName is an HTML string containing the name, googleMapsUri is the URL for the red cross location, and adrFormatAddress is the address",
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
        red_cross = await make_request_post("https://places.googleapis.com/v1/places:searchText", headers={
            "X-Goog-Api-Key": API_KEY,
            "X-Goog-FieldMask": "places.displayName,places.googleMapsUri,places.adrFormatAddress"
        }, data={
            "textQuery": "Red Cross",
        })

        print(red_cross)
      
        
        if red_cross:
            return json.dumps(red_cross)
        return "Something Went Wrong."

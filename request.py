import requests

# Your API URL
url = "https://api.web.myhq.in/meeting-room/web/list-slug"

# Input data to be sent in POST request
input_data = {
    "url": "/hyderabad/meeting-room/hyderabad",
    "selectedFilters": {
        "PRODUCT": "MEETING_ROOM",
        "CITY": "hyderabad",
        "LOCALITIES": [],
        "CAPACITY": 6,
        "DATE_DURATION_TIME": {
            "BOOKING_DATE": "2025-04-08T18:30:00.000Z",
            "DURATION": 1,
            "TIME_SLOT": []
        },
        "SORT_BY": "POPULARITY",
        "EQUIPMENTS": [],
        "BRANDS": [],
        "PRICE_RANGE": {
            "range": [499, 8000]
        },
        "AMENITIES": []
    },
    "pageNo": 1,
    "pageLimit": 16
}

# Make the POST request
response = requests.post(url, json=input_data)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print("Data received successfully!")
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
    data = None

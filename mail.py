import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
def send_workspace_email(results, sender_email, receiver_email, input_data: dict,app_password, timings):
    city = input_data["selectedFilters"]["CITY"].title()
    capacity = input_data["selectedFilters"]["CAPACITY"]
    raw_date = input_data["selectedFilters"]["DATE_DURATION_TIME"]["BOOKING_DATE"]

    # Convert date to '8th April 2025' format
    dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    day = dt.day
    suffix = "th" if 11 <= day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
    formatted_date = dt.strftime(f"%-d{suffix} %B %Y")
    msg = MIMEMultipart()
    msg['Subject'] = 'Workspace Options from myHQ'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    workspace_blocks = ""
    for i, res in enumerate(results, 1):
        workspace = res["name"]
        address = f'{res["location"]}, {res["city"]}'
        meeting_room = f'{res["capacity"]}-Seater Room'
        hours = res["duration"]
        price_per_hour = res["pricePerHour"]
        total_price = res["totalPrice"]
        amenities = res.get("amenities", "Amenities not listed.")
        photo_links = res.get("photos", [])
        link = res.get("link", "#")

        # Create photo section
        photos_html = "".join(
            f'<img src="{photo}" alt="Room Photo" style="width:200px; height:auto; margin-right:10px; margin-bottom:10px; border:1px solid #ccc; border-radius:8px;" />'
            for photo in photo_links
        )

        price_table = f"""
        <table style="border-collapse: collapse; width: 100%;">
          <tr style="background-color: #0072CE; color: white;">
            <th style="border: 1px solid black; padding: 8px;">Meeting Room</th>
            <th style="border: 1px solid black; padding: 8px;">Total no. of hours</th>
            <th style="border: 1px solid black; padding: 8px;">Per hour price (₹)</th>
            <th style="border: 1px solid black; padding: 8px;">Total Price (₹)</th>
          </tr>
          <tr>
            <td style="border: 1px solid black; padding: 8px;">1</td>
            <td style="border: 1px solid black; padding: 8px;">{hours}</td>
            <td style="border: 1px solid black; padding: 8px;">{price_per_hour}</td>
            <td style="border: 1px solid black; padding: 8px;">{total_price}</td>
          </tr>
        </table>
        """

        block = f"""
        <p><strong>Workspace Details {i:02}:</strong><br>
        Workspace: {workspace}<br>
        Address: {address}<br>
        Meeting Room: {meeting_room}<br>
        <a href="{link}">View Workspace</a><br>
        <strong>Price:</strong></p>

        {price_table}

        <p><strong>Amenities Included:</strong> {amenities}</p>

        <p><strong>Photos:</strong><br>{photos_html}</p>
        """

        workspace_blocks += block

    html_body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <p>Hi,</p>

    <p>It was nice connecting with you over the call. Thank you for sharing your requirements with us. We are glad you chose us to fulfil your workspace needs. As discussed, I am sharing the complete details below with the options for your reference.</p>

    <p><strong>Reconfirming Requirements</strong><br>
    Dates: {formatted_date}<br>
    Timings: {timings}<br>
    Location: {city}<br>
    No. of Pax: {capacity}</p>

    {workspace_blocks}

    <p><strong>Brief intro about myHQ:</strong><br>
    We, at myHQ, are helping individuals and teams work more productively in this new normal of remote working through our tech-enabled flexible workspace solutions. Instead of bringing the employee to the office, we help you take the office to the employee! myHQ is the largest coworking marketplace with over 800+ coworking spaces across the country.</p>

    <p><strong>Meeting Rooms:</strong> Hold your client meetings, workshops or get your team to present in our fully-serviced meeting rooms. Book on-demand by the hour, and ensure your meeting runs smoothly. It is cheaper than even a cup of coffee in some places – starting at ₹250 per seat per day, available across India!</p>

    <p>Website Link: <a href="https://www.myhq.in">Click here to find your desired meeting room</a></p>

    <p><strong>Why corporates choose us:</strong></p>
    <ul>
    <li>Access to 200+ meeting rooms across India</li>
    <li>Pay-Per-Use pricing (e.g., WeWork from ₹250/hour/person)</li>
    <li>No fixed monthly rental</li>
    <li>Free unlimited WiFi, Tea/Coffee</li>
    <li>No lock-in, deposit, or minimum commitment</li>
    </ul>

    <p><strong>Some of our clients:</strong> Meesho, VTION, Khalsa Aid, Ask Media, Transfive, Squadstack, Sennheiser, Mother Dairy</p>

    <p>Hope this helps! Feel free to call me at +91-9266777965. We'd be happy to assist you further. :)</p>

    <p>Best regards,<br>
    Ayaan Gautam<br>
    Associate - Sales (myHQ)<br>
    Upflex Anarock India Pvt. Ltd.<br>
    7th Floor, Building No. 9B, DLF Cyber City, Phase III, Gurgaon 122002<br>
    M: +91-9266777965<br>
    W: <a href="https://www.myhq.in">www.myhq.in</a></p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())

    print("Email sent successfully!")

# You can call this function with your results array now


results = [
  {
    "name": "Awfis",
    "location": "Gachibowli, Hyderabad",
    "city": "Hyderabad",
    "timings": "08:00 am to 08:00 pm - Monday to Saturday",
    "status": "LIVE",
    "capacity": "6",
    "pricePerHour": 1200,
    "duration": 1,
    "totalPrice": 1200,
    "amenities": "Wifi, TV(with HDMI), Whiteboard, Tea & Coffee (Unlimited on self service)",
    "link": "https://myhq.in/meeting-room/awfis-rajapushpa-summit?capacity=6&bookingType=ONLINE_INSTANT&date=2025-04-08T18:30:00.000Z",
    "photos": [
      "https://res.cloudinary.com/myhq/image/upload/mmqbnh2gyhrfervcadt5.jpg"
    ]
  },
  {
    "name": "Oyo Workflo",
    "location": "HITEC City, Hyderabad",
    "city": "Hyderabad",
    "timings": "08:00 am to 08:00 pm - Monday to Saturday",
    "status": "LIVE",
    "capacity": "10",
    "pricePerHour": 1000,
    "duration": 1,
    "totalPrice": 1000,
    "amenities": "Wifi, TV(with HDMI), Whiteboard, Tea & Coffee (Unlimited on self service)",
    "link": "https://myhq.in/meeting-room/oyo-workflo-bizness-square?capacity=10&bookingType=ONLINE_INSTANT&date=2025-04-08T18:30:00.000Z",
    "photos": [
      "https://res.cloudinary.com/myhq/image/upload/workspaces/oyo-workflo-bizness-square/meeting-room/plans/10-seater/vayuca.jpg"
    ]
  },
  {
    "name": "Apeejay Business Centre",
    "location": "Somajiguda, Hyderabad",
    "city": "Hyderabad",
    "timings": "10:00 am to 07:00 pm - Monday to Saturday",
    "status": "LIVE",
    "capacity": "8",
    "pricePerHour": 799,
    "duration": 1,
    "totalPrice": 799,
    "amenities": "Wifi, TV(with HDMI), Whiteboard, Tea & Coffee (Unlimited on self service)",
    "link": "https://myhq.in/meeting-room/apeejay-business-centre-the-park?capacity=8&bookingType=ONLINE_INSTANT&date=2025-04-08T18:30:00.000Z",
    "photos": [
      "https://res.cloudinary.com/myhq/image/upload/workspaces/apeejay-business-centre-the-park/meeting-room/plans/8-seater/3tdgbu.jpg"
    ]
  },
  {
    "name": "Awfis",
    "location": "HITEC City, Hyderabad",
    "city": "Hyderabad",
    "timings": "08:00 am to 08:00 pm - Monday to Saturday",
    "status": "LIVE",
    "capacity": "8",
    "pricePerHour": 1200,
    "duration": 1,
    "totalPrice": 1200,
    "amenities": "Wifi, TV(with HDMI), Whiteboard, Tea & Coffee (Unlimited on self service)",
    "link": "https://myhq.in/meeting-room/awfis-n-heights-3?capacity=8&bookingType=ONLINE_INSTANT&date=2025-04-08T18:30:00.000Z",
    "photos": [
      "https://res.cloudinary.com/myhq/image/upload/workspaces/awfis-n-heights-3/meeting-room/plans/8-seater/suv9ya.jpg",
      "https://res.cloudinary.com/myhq/image/upload/workspaces/awfis-n-heights-3/meeting-room/plans/8-seater/paw5ga.jpg"
    ]
  },
  {
    "name": "Awfis",
    "location": "Gachibowli, Hyderabad",
    "city": "Hyderabad",
    "timings": "08:00 am to 08:00 pm - Monday to Saturday",
    "status": "LIVE",
    "capacity": "9",
    "pricePerHour": 1500,
    "duration": 1,
    "totalPrice": 1500,
    "amenities": "Wifi, TV(with HDMI), Whiteboard, Tea & Coffee (Unlimited on self service)",
    "link": "https://myhq.in/meeting-room/awfis-rajapushpa-summit?capacity=9&bookingType=ONLINE_INSTANT&date=2025-04-08T18:30:00.000Z",
    "photos": [
      "https://res.cloudinary.com/myhq/image/upload/cbqedesjskzgkyqbactg.jpg"
    ]
  }
]

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
            "range": [
                499,
                8000
            ]
        },
        "AMENITIES": []
    },
    "pageNo": 1,
    "pageLimit": 16
}
sender_email = "rahulnanda614@gmail.com"
receiver_email = "kuwarjain394@gmail.com"
app_password = 'ehto ilok wsaw bxyf'

timings = "10:00 AM to 5:00 PM"
send_workspace_email(results, sender_email, receiver_email ,input_data, app_password,timings)
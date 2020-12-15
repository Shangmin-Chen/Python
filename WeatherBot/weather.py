# Weather Bot made in AP COMSCI class using API from openweather.com
import requests
import json
from PIL import Image, ImageFont, ImageDraw
from datetime import date

api_key = "59d0def3cb08927692cbc6416900eab4"
position = [300, 430, 555, 690, 825]

# list of cities
us_list = ["New York", "Chicago", "San Francisco", "Los Angeles", "San Diego"]
china_list = ["Shanghai", "Wuhan", "Chengdu", "Fuzhou", "Hangzhou"]
russia_list = ["Moscow", "Saint Petersburg", "Novosibirsk", "Kazan", "Volgograd"]

# below is the code that was used in class


def countryfunc(city_list, country):
    for cities in city_list:
        image = Image.open("post.png")
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("Inter.ttf", size=50)
        content = "Latest Weather Forecast"
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 77)
        draw.text((x, y), content, color, font=font)

        font = ImageFont.truetype("Inter.ttf", size=30)
        today = date.today()
        content = date.today().strftime("%A - %B %d, %Y")
        color = "rgb(255, 255, 255)"
        (x, y) = (46, 145)
        draw.text((x, y), content, color, font=font)

    index = 0
    for city in cities:
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial".format(city, api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        #city
        font = ImageFont.truetype("Inter.ttf", size=50)
        color = "rgb(0, 0, 0)"
        (x, y) = (135, position[index])
        draw.text((x, y), city, color, font=font)

        #temp
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = "rgb(255, 255, 255)"
        (x, y) = (600, position[index])
        draw.text((x, y), content, color, font=font)

        #humidity
        font = ImageFont.truetype("Inter.ttf", size=50)
        content = str(data["main"]["humidity"]) + "%"
        color = "rgb(255, 255, 255)"
        (x, y) = (810, position[index])
        draw.text((x, y), content, color, font=font)

        index += 1
    image.save(country + "cities_pd5.png")


# calling the function


countryfunc([us_list], "us")
countryfunc([china_list], "cn")
countryfunc([russia_list], "ru")

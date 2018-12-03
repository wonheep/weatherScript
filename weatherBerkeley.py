#API: https://darksky.net/dev

from datetime import timedelta, date
import requests
import csv
import json

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def main():

	start_date = date(2008, 1, 1)
	end_date = date(2009, 1, 1)

	f = csv.writer(open("weather_dailydata_Berkeley_2008.csv", "a+"))

	# Write CSV Header, If you dont need that, remove this line
	f.writerow(["date",
				"latitude",
				"longitude",
				"timezone",
				"time",
				"summary",
				"icon",
				"sunriseTime",
				"sunsetTime",
				"moonPhase",
				"precipIntensity",
				"precipIntensityMax",
				"precipProbability",
				"temperatureHigh",
				"temperatureHighTime",
				"temperatureLow",
				"temperatureLowTime",
				"apparentTemperatureHigh",
				"apparentTemperatureHighTime",
				"apparentTemperatureLow",
				"apparentTemperatureLowTime",
				"dewPoint",
				"humidity",
				"pressure",
				"windSpeed",
				"windGust",
				"windGustTime",
				"windBearing",
				"cloudCover",
				"uvIndex",
				"uvIndexTime",
				"visibility",
				"temperatureMin",
				"temperatureMinTime",
				"temperatureMax",
				"temperatureMinTime",
				"apparentTemperatureMin",
				"apparentTemperatureMinTime",
				"apparentTemperatureMax",
				"apparentTemperatureMaxTime",
				"offset"])

	for single_date in daterange(start_date, end_date):
		print(single_date.strftime("%Y-%m-%d"))

		base_url = 'https://api.darksky.net/forecast/9504545ecfaa62db3db95544cd07c4a3/37.8690,-122.2704,'
		end_url = 'T00:00:00'
		URL = base_url+str(single_date)+end_url
		print(URL)

		language = 'en'
		fields_exclude = 'currently,minutely,hourly,alerts,flags'
		PARAMS = {'exclude':fields_exclude, 'lang':language} 

		# sending get request and saving the response as response object 
		resp = requests.get(url = URL, params = PARAMS) 

		# extracting data in json format 
		json_parsed = json.loads(resp.text)
		print(json_parsed)

		f.writerow([single_date,
					json_parsed["latitude"],
					json_parsed["longitude"],
					json_parsed["timezone"],
					json_parsed["daily"]["data"][0]["time"],
					json_parsed["daily"]["data"][0]["summary"],
					json_parsed["daily"]["data"][0]["icon"],
					json_parsed["daily"]["data"][0]["sunriseTime"],
					json_parsed["daily"]["data"][0]["sunsetTime"],
					json_parsed["daily"]["data"][0]["moonPhase"],
					json_parsed["daily"]["data"][0]["precipIntensity"],
					json_parsed["daily"]["data"][0]["precipIntensityMax"],
					json_parsed["daily"]["data"][0]["precipProbability"],
					json_parsed["daily"]["data"][0]["temperatureHigh"],
					json_parsed["daily"]["data"][0]["temperatureHighTime"],
					json_parsed["daily"]["data"][0]["temperatureLow"],
					json_parsed["daily"]["data"][0]["temperatureLowTime"],
					json_parsed["daily"]["data"][0]["apparentTemperatureHigh"],
					json_parsed["daily"]["data"][0]["apparentTemperatureHighTime"],
					json_parsed["daily"]["data"][0]["apparentTemperatureLow"],
					json_parsed["daily"]["data"][0]["apparentTemperatureLowTime"],
					json_parsed["daily"]["data"][0]["dewPoint"],
					json_parsed["daily"]["data"][0]["humidity"],
					json_parsed["daily"]["data"][0]["pressure"],
					json_parsed["daily"]["data"][0]["windSpeed"],
					json_parsed["daily"]["data"][0]["windGust"],
					json_parsed["daily"]["data"][0]["windGustTime"],
					json_parsed["daily"]["data"][0]["windBearing"],
					json_parsed["daily"]["data"][0]["cloudCover"],
					json_parsed["daily"]["data"][0]["uvIndex"],
					json_parsed["daily"]["data"][0]["uvIndexTime"],
					json_parsed["daily"]["data"][0]["visibility"],
					json_parsed["daily"]["data"][0]["temperatureMin"],
					json_parsed["daily"]["data"][0]["temperatureMinTime"],
					json_parsed["daily"]["data"][0]["temperatureMax"],
					json_parsed["daily"]["data"][0]["temperatureMinTime"],
					json_parsed["daily"]["data"][0]["apparentTemperatureMin"],
					json_parsed["daily"]["data"][0]["apparentTemperatureMinTime"],
					json_parsed["daily"]["data"][0]["apparentTemperatureMax"],
					json_parsed["daily"]["data"][0]["apparentTemperatureMaxTime"],
					json_parsed["offset"]])

if __name__ == "__main__":
    main()



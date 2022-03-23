class WeatherModel:
    def __init__(self, date, temp):
        self.date = date[8:10] + "." + date[5:7] + "." + date[:4]
        self.temp = temp

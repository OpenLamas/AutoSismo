class Earthquake:

    def __init__(self, table):
        date_time = table[0].split("T")

        self.date = date_time[0]
        self.time = date_time[1]
        self.latitude = table[1]
        self.longitude = table[2]
        self.depth = table[3]
        self.mag = table[4]
        self.place = table[13]
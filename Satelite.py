class Satelite:
    def __init__(self, id, observation_cost, transmission_cost, rotation_cost, charge_power, battery, position):
        self.id = id
        self.position = position
        self.observation_cost = observation_cost
        self.transmission_cost = transmission_cost
        self.rotation_cost = rotation_cost
        self.charge_power = charge_power
        self.battery = battery
        self.max_battery = battery
        self.observation_completed = []

    def do_nothing(self):
        return

    def take_observation(self):
        self.battery =- self.observation_cost
        return

    def rotate(self):
        if self.id == 1:
            self.rotate1()
        else:
            self.rotate2()

    def rotate1(self):
        if self.position == 1:
            self.position = 0
        elif self.position == 0:
            self.position = 1

    def rotate1(self):
        if self.position == 1:
            self.position = 2
        elif self.position == 2:
            self.position = 1

    # def charge(self):
    #     self.battery =+ self.charge_power

    def __str__(self):
        return str(self.observation_cost) + str(self.transmission_cost) + str(self.rotation_cost) + str(self.charge_power) + str(self.battery)
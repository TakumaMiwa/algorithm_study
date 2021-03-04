class Secretary:
    def __init__(self):
        self.appointment = {}

    def request_appointment(self, when, who):
        if (when in self.appointment):
            return False
        else:
            self.appointment[when] = who
            return True

    def get_schedule(self):
        return str(self.appointment)


class Manager:
    def __init__(self):
        self.sara = Secretary()

    def check_schedule(self):
        schedule = self.sara.get_schedule()
        print(schedule)

    def get_secretary(self):
        return self.sara


class Client:
    def __init__(self, name):
        self.name = name
        self.contact_point = None

    def set_contact_point(self, contact_point):
        self.contact_point = contact_point

    def make_appointment(self, when):
        if self.contact_point:
            is_success = self.contact_point.request_appointment(when, self.name)
            print(self.name + "could book?: " + str(is_success))


bob = Manager()

adam = Client('adam')
adam.set_contact_point(bob.get_secretary())
adam.make_appointment('10:30')

charles = Client('charles')
charles.set_contact_point(bob.get_secretary())
charles.make_appointment(('11:30'))

dag = Client('dag')
dag.set_contact_point(bob.get_secretary())
dag.make_appointment('10:30')
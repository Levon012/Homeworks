"""Create a Python class representing a Hospital account with methods to schedule visit
and remove schedule."""


class HospitalAccount:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
    def schedule_visit(self):
        return f'{self.patient} visit scheduled with Doctor {self.doctor} on {self.date} at {self.time}.'
    def remove_visit(self):
        return f'{self.patient} visit with Doctor {self.doctor} on {self.date} at {self.time} has been removed.'

account = HospitalAccount('Edmon Hakobyan', 'Axajanyan', '29.08.2024', '11-00')
print(account.schedule_visit())
print(account.remove_visit())



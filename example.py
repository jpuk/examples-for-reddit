class Staff():
    def __init__(self, first_name, last_name, job_title, salary=None):
        if salary:
            self._salary = salary
        else:
            self._salary = 0.0
        self._job_title = job_title
        self._first_name = first_name
        self._last_name = last_name
        self._job_title = job_title
        self.create_user_account()

    def update_salary(self, amount):
        # code to interact with finance system and check staff pay bands etc
        # is this a valid salary for role, etc, etc
        self._salary = amount

    def get_salary(self):
        print("{} {} has a salary of {}".format(self._first_name,
                                                self._last_name, self._salary))
        return self._salary

    def change_role(self, new_title):
        # code to check this matches a valid role here, etc
        self._job_title = new_title

    def update_name(self, first, last):
        self._first_name = first
        self._last_name = last
        # interact with the online service and Windows domain
        # server to check username is free, etc

    def create_user_account(self):
        self._username = self._first_name[:1] + self._last_name
        # interact with the online service and Windows domain
        # server to check username is free, etc
        print("Some code here that creates the user account {}".format(self._username))

    def remove_user_account(self):
        print("Some code here that deletes user account {}.".format(self._username))


my_staff = []
print(type(my_staff))
my_staff.append(Staff("John", "Doe", "IT Manager", salary=50000))
my_staff.append(Staff("Jane", "Smith", "IT Director", salary=75000))

for individual in my_staff:
    print(individual.get_salary())

for staff in my_staff:
    individual.remove_user_account()
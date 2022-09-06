import datetime

# Employee class
class Employee:
    def __init__(self):
        self.name = get_name()
        self.start_date = get_start_date()
        self.end_date = get_end_date(self.start_date)
        self.hours_worked = get_hrs_worked()
        self.hr_rate = get_hourly_rate()
        self.tax_rate = get_tax_rate()

        self.gross_pay = None
        self.income_tax = None
        self.net_pay = None

# Data entry: name
def get_name():
    running = True
    while running:
        name: str = input("Enter employee name: ")
        if len(name) == 0:
            continue
        elif name.isdigit():
            continue
        else:
            running = False
    return name

# data entry: start_date for work period
def get_start_date():
    running = True
    while running:
        data_entry = input("Enter start date(mm/dd/yyyy): ")
        try:
            month, day, year = map(int, data_entry.split('/'))
            start_date = datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Enter '(mm/dd/yyyy)'")
            continue
        else:
            running = False
    return start_date

# data entry: end_date for work period
def get_end_date(start_date):
    running = True
    while running:
        date_entry = input("Enter end date(mm/dd/yyyy): ")
        try:
            month, day, year = map(int, date_entry.split('/'))
            end_date = datetime.date(year, month, day)
        except ValueError:
            print("Invalid date format. Enter '(mm/dd/yyyy)'")
            continue
        if end_date < start_date:
            print("Invalid date range.")
            continue
        else:
            running = False
    return end_date

# Data entry: hours worked by employee
def get_hrs_worked():
    running = True
    while running:
        try:
            hrs = float(input("Enter hours worked: "))
        except ValueError:
            continue
        if hrs is not None:
            running = False
    return hrs

# Date entry: hourly rate
def get_hourly_rate():
    running = True
    while running:
        try:
            rate = float(input("Enter hourly rate: "))
        except ValueError:
            continue
        if rate is not None:
            running = False
    return rate

# Data entry: income tax rate
def get_tax_rate():
    running = True
    while running:
        try:
            tax = float(input("Enter income tax rate: "))
        except ValueError:
            continue
        if tax is not None:
            running = False
    return tax

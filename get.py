import datetime
import locale


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


def new_entry():
    running = True
    while running:
        try:
            again = str(input('Enter \'Start\' to enter employee payroll information  \n'
                              'or     \'End\'  to exit application\n'))
        except ValueError:
            continue
        if again.lower() == 'start':
            return True
        elif again.lower() == 'end':
            return False


# net salary calculator
def net_cal(hours_worked, hr_rate, tax_rate):
    gross_pay = hours_worked * hr_rate
    income_tax = (gross_pay * tax_rate) / 100
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay


# exit summary
def emp_summary(employee):
    employee.gross_pay, employee.income_tax, employee.net_pay = net_cal(employee.hours_worked, employee.hr_rate,
                                                                        employee.tax_rate)

    locale.setlocale(locale.LC_ALL, "en_US")

    print(f"\n     Employee: {employee.name}")
    print(f"  Work period: {employee.start_date.strftime('%m/%d/%y')} - {employee.end_date.strftime('%m/%d/%y')}")
    print(f"  Total Hours: {employee.hours_worked}")
    print(f"  Hourly Rate: {employee.hr_rate}")
    print(f"     Tax Rate: {employee.tax_rate}%")
    print(f"   Income Tax: {locale.currency(employee.income_tax)}")
    print(f"      Net Pay: {locale.currency(employee.net_pay)}\n")


# creating and storing list totals into total_ref dict.
# called in end_totals_report()
def end_totals(emp_list):
    emp_total = len(emp_list)
    hrs_worked = sum((float(employee.hours_worked) + float(emp_list['hours_worked'])) for emp in emp_list)
    # locale.setlocale(locale.LC_ALL, "en_US")
    # gross_f = locale.currency(sum(emp_list['gross_pay'] for emp in emp_list))
    # income_tax_f = locale.currency(sum(emp_list['income_tax'] for emp in emp_list))
    # net_f = locale.currency(sum(emp_list['net_pay'] for emp in emp_list))

    total_ref = {
        "employed": emp_total,
        # "hours": hrs_worked
        # "gross": gross_f,
        # "tax": income_tax_f,
        # "net": net_f
    }
    return total_ref


# summary report --> totals_ref dict.
def end_totals_report(emp_list):
    totals = end_totals(emp_list)

    print(f"\n     Total employed: {totals['employed']}")
    print(emp_list)
    # print(f"       Hours worked: {totals['hours']} ")
    # print(f"        Total Gross: {totals['gross']}")
    # print(f"         Income tax: {totals['tax']}")
    # print(f"          Total net: {totals['net']}\n")

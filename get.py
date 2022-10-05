import datetime
import locale
import f_handling as f
import Employee as e


def new_entry():
    running = True
    while running:
        try:
            again = str(input('Enter \'Start\' to enter employee payroll information  \n'
                              'or     \'End\'  for Payroll Summary Report\n'))
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
    return employee

def convert_vals():
    emp_list = f.read_file()
    for dicts in emp_list:
        for keys in dicts:
            if keys == 'hours_worked':
                dicts['hours_worked'] = float(dicts['hours_worked'])

            elif keys == 'hr_rate':
                dicts['hr_rate'] = float(dicts['hr_rate'])

            elif keys == 'tax_rate':
                dicts['tax_rate'] = float(dicts['tax_rate'])

            elif keys == 'gross_pay':
                dicts['gross_pay'] = float(dicts['gross_pay'])

            elif keys == 'income_tax':
                dicts['income_tax'] = float(dicts['income_tax'])

            elif keys == 'net_pay':
                dicts['net_pay'] = float(dicts['net_pay'])
    return emp_list

def print_header():
    print(f"{'Worked From':10} | {'Worked To':10}  | {'Employee Name':15}  | {'Hours Worked':8}  | {'Hourly Rate':8}  | "
          f"{'Tax Rate':8}  | {'Gross Pay':8}  | {'Taxes Paid':8}  | {'Net Pay':8}")


def date_range_report(emp_list):
    print_opt = input("Enter 'ALL' for full employee report or "
                      "Press enter to specify date ")

    if print_opt.lower() == 'all':
        print()
        print_header()
        for emp in emp_list:
            print(f"{emp['start_date']:13} {emp['end_date']:13} {emp['name']:21} {emp['hours_worked']:5.2f} "
                  f"{emp['hr_rate']:16.2f} {emp['tax_rate']:11.2f} {emp['gross_pay']:13.2f} "
                  f"{emp['income_tax']:12.2f} {emp['net_pay']:11.2f}")

    else:
        start_date = e.get_start_date()
        start = start_date.strftime('%Y-%m-%d')
        print()
        print_header()
        for emp in emp_list:
            if start <= emp['start_date']:
                print(f"{emp['start_date']:13} {emp['end_date']:13} {emp['name']:21} {emp['hours_worked']:5.2f} "
                      f"{emp['hr_rate']:16.2f} {emp['tax_rate']:11.2f} {emp['gross_pay']:13.2f} "
                      f"{emp['income_tax']:12.2f} {emp['net_pay']:11.2f}")


def end_totals(emp_list):
    emp_total = len(emp_list)
    hrs_worked = sum(emp['hours_worked'] for emp in emp_list)
    locale.setlocale(locale.LC_ALL, "en_US")
    gross_f = locale.currency(sum(emp['gross_pay'] for emp in emp_list))
    income_tax_f = locale.currency(sum(emp['income_tax'] for emp in emp_list))
    net_f = locale.currency(sum(emp['net_pay'] for emp in emp_list))

    total_ref = {
        "employed": emp_total,
        "hours": hrs_worked,
        "gross": gross_f,
        "tax": income_tax_f,
        "net": net_f
    }
    return total_ref


# summary report --> totals_ref dict.
def end_totals_report(emp_list):
    totals = end_totals(emp_list)

    print(f"\n     Total employed: {totals['employed']}")
    print(f"       Hours worked: {totals['hours']} ")
    print(f"        Total Gross: {totals['gross']}")
    print(f"         Income tax: {totals['tax']}")
    print(f"          Total net: {totals['net']}\n")
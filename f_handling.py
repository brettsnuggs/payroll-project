import csv  # read, parse, and write to a file - delimiter '|'
import get
file = 'emp_info.txt'


### reads employee tuple from file
## appends to list()
# returns list() -->
def init_list():
    emp_list = []
    with open(file, 'r') as f:
        reader = csv.DictReader(f, delimiter='|')
        for line in reader:
            emp_list.append(line)
            gross_pay, income_tax, net_pay = get.net_cal(float(line['hours_worked']), float(line['hr_rate']),
                                                         float(line['tax_rate']))
            line['gross_pay'] = gross_pay
            line['income_tax'] = income_tax
            line['net_pay'] = net_pay

        return emp_list


# parse emp_summary to emp_info.txt
def append_emp(emp_summary):
    with open(file, 'a', newline='') as f:
        fieldnames = ['start_date', 'end_date', 'name', 'hours_worked', 'hr_rate', 'tax_rate', 'gross_pay',
                      'income_tax', 'net_pay']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')

        writer.writerow({'start_date': emp_summary.start_date,
                         'end_date': emp_summary.end_date,
                         'name': emp_summary.name,
                         'hours_worked': emp_summary.hours_worked,
                         'hr_rate': emp_summary.hr_rate,
                         'tax_rate': emp_summary.tax_rate,
                         'gross_pay': emp_summary.gross_pay,
                         'income_tax': emp_summary.income_tax,
                         'net_pay': emp_summary.net_pay})

def read_file():
    emp_list = []
    with open(file, 'r', newline='') as f:
        fieldnames = ['start_date', 'end_date', 'name', 'hours_worked', 'hr_rate', 'tax_rate', 'gross_pay',
                      'income_tax', 'net_pay']
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter='|')
        next(reader)
        for line in reader:
            emp_list.append(line)
    return emp_list


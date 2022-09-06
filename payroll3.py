# Brett Snuggs, CIS 261, Course Project Part 2
import get as g
import f_handling as f
import Employee as e

def main():
    emp_list = f.init_list()  # initialize list from file --> employee info
    running = True
    while running:
        for i in range(100):
            emp = e.Employee()
            emp_summary = g.emp_summary(emp)
            f.append_emp(emp_summary)
            emp_list.append(emp_summary)
            i += 1

            again = g.new_entry()
            if again:
                running = True
            else:

                emp_list = g.convert_vals()
                g.date_range_report(emp_list)
                g.end_totals_report(emp_list)
                running = False
                break


if __name__ == "__main__":
    main()

# Brett Snuggs, CIS 261, Course Project Part 2
import get as g
import f_handling as f
import Employee as e
import login

def main():
    emp_list = f.init_list()  # initialize list from file --> employee info
    user_auth_code = login.login()

    running = True
    while running:

        if user_auth_code == 'admin':
            for i in range(100):
                emp = e.Employee()
                emp_summary = g.emp_summary(emp)
                f.append_emp(emp_summary)
                emp_list.append(emp_summary)
                i += 1

                again = g.new_entry()

                if again:
                    running = True

                elif not again:
                    emp_list = g.convert_vals()
                    g.date_range_report(emp_list)
                    g.end_totals_report(emp_list)
                    break

        elif user_auth_code == 'user':
            emp_list = g.convert_vals()
            g.date_range_report(emp_list)
            g.end_totals_report(emp_list)
            continue



if __name__ == "__main__":
    main()

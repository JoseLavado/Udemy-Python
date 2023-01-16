
work_hours =[ ("Moe", 1000), ("Mike", 2000), ("Jose", 5000), ("Steve", 500)]


def top_employee(employees):
    current_max = 0
    top_guy = ""

    for name, hours in employees:
        if hours > current_max:
            current_max = hours
            top_guy = name
        else:
            pass
    return(top_guy, current_max)


print (top_employee(work_hours))






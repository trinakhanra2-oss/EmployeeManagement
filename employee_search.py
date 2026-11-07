# Employee Search Feature

employees = [
    {
        "name": "Sana",
        "email": "sana@gmail.com"
    },
    {
        "name": "Riya",
        "email": "riya@gmail.com"
    }
]


def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    return "Employee Not Found"


if __name__ == "__main__":
    result = search_employee("Sana")
    print(result)

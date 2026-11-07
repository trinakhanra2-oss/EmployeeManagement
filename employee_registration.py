# Employee Registration Feature

def register_employee(name, email):
    employee = {
        "name": name,
        "email": email
    }

    return employee


if __name__ == "__main__":
    result = register_employee(
        "Sana",
        "sana@gmail.com"
    )

    print("Employee Registered Successfully")
    print(result)

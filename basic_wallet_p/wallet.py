import json


def load():
    with open("./cache.json") as f:
        data = json.load(f)
    return data


def save(data):
    file = open("./cache.json", "w")
    file.write(str(json.dumps(data)))
    file.close()


def main():
    data = load()
    if "id" not in data:
        id = input("hello, enter a user id:")
        data["id"] = id
    else:
        print(f"Welcome back {data['id']}")

    while True:
        menu = [
            "Choose an Option",
            "*Change ID: 1",
            "*Check Balance: 2",
            "*Manage Transactions: 3",
        ]
        for item in menu:
            print(item)
        option = input()

        if option == "1":
            id = input("Enter New ID:")
            data["id"] = id

        elif option == "2":
            print(f"Your balance is {data['balance']}")
        elif option == "3":
            menu = [
                "Choose an Option",
                "*View Transactions: 1",
                "*Make a Transaction: 2",
            ]
            for item in menu:
                print(item)
            option = input()

            if option == "1":
                print(data["transactions"])

            elif option == "2":
                to = input("Who are you sending the money to?:")
                amount = int(input("How much are you sending?"))
                transaction = {"from": data["id"], "to": to, "amount": amount}
                data["balance"] -= amount

                data["transactions"].append(transaction)

        save(data)


main()

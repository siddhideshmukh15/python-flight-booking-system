flights={
    "1": {"name": "Nagpur to Delhi",
          "price": 4500,"seats":10},
    "2": {"name": "Nagpur to Mumbai",
          "price": 3000,"seats":10},
    "3": {"name": "Nagpur to pune",
          "price": 2500,"seats":10}
}

while True:
    print("\n==== Flight Booking ====")
    print("1.'View Flights' \n2.'Book Flight'\n3.'Exit'")
    
    choice =input("Enter choice:")
    
    if choice =="1":
        for key,flight in flights.items():
            print(key,
                  flight["name"],"-",
                  flight["price"],
                         "- seats:",
                         flight["seats"])
            
    elif choice =="2":
        key=input("select flight:")
        
        if key in flights:
            tickets=int(input("Enter tickets:"))
            
            if tickets <= flights[key]["seats"]:
                name=input("Enter passenger name:")
                total=tickets*flights[key]["price"]
                flights[key]["seats"]-= tickets
                
                print("\n Booking Successful!")
                print("Passenger:",name)
                print("Flight:",flights[key]["name"])
                print("Tickets:",tickets)
                print("Total: rs",total)
                
            else:
                print("Invalid flight!")
                
    elif choice =="3":
        print("Thank you!")
        print("pls visit again!")
        break
    
    else:
        print("Invalid choice!")
            
            
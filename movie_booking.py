movies = {
    1: ["Leo", 250],
    2: ["Jawan", 300],
    3: ["Pathaan", 280],
}

seats = {}
for m in movies:
    seats[m] = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4"]

bookings = []


def show_movies():
    print("\nMovies available:")
    for k in movies:
        print(k, "-", movies[k][0], "- Rs.", movies[k][1])


def book():
    show_movies()
    try:
        m = int(input("Choose movie number: "))
    except ValueError:
        print("Invalid input")
        return
    if m not in movies:
        print("Movie not found")
        return

    print("Free seats:", seats[m])
    chosen = input("Enter seats separated by space: ").upper().split()

    if len(chosen) == 0:
        print("No seats selected")
        return
    for s in chosen:
        if s not in seats[m]:
            print("Seat", s, "is not available")
            return

    name = input("Your name: ")
    total = len(chosen) * movies[m][1]
    for s in chosen:
        seats[m].remove(s)

    bookings.append([name, movies[m][0], chosen, total])
    print("\n----- TICKET -----")
    print("Name:", name)
    print("Movie:", movies[m][0])
    print("Seats:", ", ".join(chosen))
    print("Total: Rs.", total)
    print("------------------")


def show_bookings():
    if len(bookings) == 0:
        print("No bookings yet")
    for b in bookings:
        print(b[0], "|", b[1], "|", ", ".join(b[2]), "| Rs.", b[3])


def cancel():
    name = input("Enter name used for booking: ")
    for b in bookings:
        if b[0] == name:
            for m in movies:
                if movies[m][0] == b[1]:
                    seats[m].extend(b[2])
            bookings.remove(b)
            print("Booking cancelled")
            return
    print("No booking found")


print("---- MOVIE BOOKING ----")
while True:
    print("\n1. Show movies")
    print("2. Book tickets")
    print("3. All bookings")
    print("4. Cancel booking")
    print("5. Exit")
    ch = input("Choose: ")
    if ch == "1":
        show_movies()
    elif ch == "2":
        book()
    elif ch == "3":
        show_bookings()
    elif ch == "4":
        cancel()
    elif ch == "5":
        print("Bye")
        break
    else:
        print("Wrong choice")

import sys
total = 40
while(True):
    if(total>0):
        print(total,"seats are available.")
        book_seats = int(input("How many seats to book?: "))
        if(book_seats<=total):
            print("Booking Successful.")
            total = total - book_seats
            book_seats = 0
        else:
            print("Insufficient Seats. Try booking again.")
            book_seats = 0
    else:
        print("All Seats Booked. Booking Window Closed.")
        sys.exit(0)
import random
import sqlite3
import string
from fpdf import FPDF

class User:
    """Represents a user that buys a cinema seat"""

    def _init_(self, name):
        self.name = name

    def buy(self, seat, card):
        """Buys the Seat if the card is Valid"""
        if seat.is_free():
            if card.validate(price=seat.get_price()):
                seat.occupy()
                # Create a Ticket object and generate a PDF
                # ticket = Ticket(user=self, price=seat.get_price(), seat_number=seat.seat_id)
                # ticket.to_pdf()
                return "Purchase was successful."
            else:
                return "There was a problem with your card."
        else:
            return"Seat is taken"


class Seat:
    """Represents a Cinema Seat that can be Purchased by a User"""
    database = "cinema.db"

    def __init__(self, seat_id):
        self.seat_id = seat_id

    def get_price(self):
        """Gets the Price of a certain Seat"""
        #Connect to the DB
        connection = sqlite3.connect(self.database)
        # Create a cursor object
        cursor = connection.cursor()
        # Create the get price query
        query = "SELECT price FROM seat WHERE seat_id =?"
        # Execute the query
        cursor.execute(query, [self.seat_id])
        # Store the price in a variable
        price = cursor.fetchall()[0][0]
        return price
    
    def is_free(self):
        """Checks in the DB if a Seat is Taken or Not"""
         #Connect to the DB
        connection = sqlite3.connect(self.database)
        # Create a cursor object
        cursor = connection.cursor()
        # Create the get price query
        query = "SELECT taken FROM seat WHERE seat_id =?"
        # Execute the query
        cursor.execute(query, [self.seat_id])
        # store the seat status in a variable
        result = cursor.fetchall()[0][0]
        # Check if the seat is taken, if so return False if taken otherwise True
        if result == 0:
            return True
        else:
            return False
        


    def occupy(self):
        """Change Value of taken in DB from 0 to 1"""
        if self.is_free():
            #Connect to the DB
            connection = sqlite3.connect(self.database)
            # Create a cursor object
            cursor = connection.cursor()
            # Create the get price query
            query = "UPDATE seat SET taken = ? WHERE seat_id =?"
            # Execute the query
            cursor.execute(query, [1, self.seat_id])
            # commit changes to the DB
            connection.commit()
            # close the db connection
            connection.close()

class Card:
    """Represents a Bank card needed to finalize a Seat Purchase"""
    database = "cinema.db"

    def __init__(self, type, number, cvc, holder):
        self.type = type
        self.number = number
        self.cvc = cvc
        self.holder = holder

    def validate(self, price):
        """Checks if card is valid and has balance, Subtract Price from balance"""
         #Connect to the DB
        connection = sqlite3.connect(self.database)
        # Create a cursor object
        cursor = connection.cursor()
        # Create the get price query
        query = "SELECT balance FROM card WHERE number =? AND cvc = ?"
        # Execute the query
        cursor.execute(query, [self.number, self.cvc])
        # store results to a variable
        result = cursor.fetchall()

        # check if we get something back
        if result:
            balance = result[0][0]
            if balance >= price:
                query = "UPDATE card SET balance = ? WHERE number = ? AND cvc = ?"
                cursor.execute(query, [balance - price, self.number, self.cvc])
                connection.commit()
                connection.close()

class Ticket:
    """Represents a Cinema Ticket Purchased by a User"""

    def __init__(self, user, price, seat_number):
        self.user = user
        self.price = price
        self.seat_number = seat_number
        self.id = "".join([random.choice(string.ascii_uppercase) for i in range(8)]) # ASH9U6D

    def to_pdf(self):
        """Creates a PDF Ticket"""



# if __name__ == '__main__':
    # Ask the user for their info before purchase
    name = input("Your Full Names: ")
    seat_id = input("Preffered Seat Number: ")
    card_type = input("Your Card Type: ")
    card_number = input("Your Card Number: ")
    card_cvc = input("Your Card cvc: ")
    card_holder = input("Card Holder Name: ")

    # Instantiate the classes / create objects
    user = User(name=name)
    seat = Seat(seat_id=seat_id)
    card = Card(type=card_type, number=card_number, cvc=card_cvc, holder=card_holder)

    # buy the seat
    print(user.buy(seat, card))

# print("".join([random.choice(string.ascii_uppercase) for i in range(8)]))
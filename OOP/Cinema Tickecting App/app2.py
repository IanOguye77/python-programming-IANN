import sqlite3
import random
# import fpdf
import string
from fpdf import FPDF
 

class User:
        """represents a use that buys cinema ticket"""
        def __init__(self,name):
            self.name = name
            
        def buy(self,seat,card):
            """buys the ticket if card is valid"""
            if seat.is_free():
                if card.validate(price=seat.get_price()):
                    seat.occupy()
                    ticket = Ticket(user = self,price = seat.get_price(),seat_number = seat_id)
                    return "purchase was succesfull"
                else:
                    return "There was a problem with your card!!!." 
            else:
                return "seat is taken"
                    
                    
                    
class Seat:
        """represents a cinema seat that a user can be taken by user"""
        database = "cinema.db"
        def __init__(self, seat_id):
            self.seat_id = seat_id
        
        def get_price(self):
            """get price of a certain seat"""
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            query = "SELECT price FROM seat WHERE seat_id = ?"
            cursor.execute(query,[self.seat_id])
            price = cursor.fetchall()[0][0]
            connection.close()
            return price
        
        def is_free(self):
            """check in database if seat is taken or not"""
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            query = "SELECT taken From seat WHERE seat_id = ?"
            cursor.execute(query,[self.seat_id])
            result = cursor.fetchall()[0][0]
            connection.close()
            
            if result == 0:
                return True
            else:
                return False
            
            
        def occupy(self):
            """change value of taken in the database from 0 to 1 if seat is free"""
            if self.is_free():
                connection = sqlite3.connect(self.database)
                cursor = connection.cursor()
                query = "UPDATE seat SET taken = ? WHERE seat_id = ?"
                cursor.execute(query,[1,self.seat_id])
                connection.commit()
                connection.close()
   
class Card:
        """represents a bank card needed to finalize a seat purchase"""
        database = "cinema.db"
        def __init__(self,type,number,cvc,holder):
            self.type = type
            self.number = number
            self.cvc = cvc
            self.holder = holder
            
        def validate(self,price):
            """checks if card is valid and has balance subtract price from balance"""
            connection = sqlite3.connect(self.database)
            cursor = connection.cursor()
            query = "SELECT balance FROM card WHERE number = ? AND cvc = ?"
            cursor.execute(query,[self.number,self.cvc])
            
            result= cursor.fetchall()
            
            if  result:
                balance = result[0][0]
                query = "UPDATE card SET balance = ? WHERE  number = ? AND cvc = ?"
                cursor.execute(query,[balance - price,self.number,self.cvc])
                connection.commit()
                connection.close()
                return True
            
class Ticket:
        """represents user ticket"""
        def __init__(self,user,price,seat_number):
            self.user = user
            self.price = price
            self.id ="".join([random.choice(string.ascii_uppercase)for i in range(8)])
            self.seat_number = seat_number
        def to_pdf(self):
            """creates a pdf ticket"""
            pdf = FPDF(orientation = "p", unit = "pt", format="A4")
            pdf.add_page()
            
            #header of pdf
            pdf.set_font(family = 'times', style= 'B',size=24)
            pdf.cell(w=0, h=80,txt="CPL DIgital Ticket",border= 1,ln=1, align="C")
            
            #name row
            pdf.set_font(family = "Times",style="B",size=14)
            pdf.cell(w=100,h=25,txt="Name: ",border=1)
            pdf.set_font(family = "Times",style="B",size=12)
            pdf.cell(w=0,h=25,txt= self.user.name,border=1,lu=1)
            
            
            #Ticket row
            pdf.set_font(family = "Times",style="B",size=14)
            pdf.cell(w=100,h=25,txt="Ticket_ID: ",border=1)
            pdf.set_font(family = "Times",style="B",size=12)
            pdf.cell(w=0,h=25,txt= self.id,border=1,lu=1)
            
            #seat row
            pdf.set_font(family = "Times",style="B",size=14)
            pdf.cell(w=100,h=25,txt="Seat_num: ",border=1)
            pdf.set_font(family = "Times",style="B",size=12)
            pdf.cell(w=0,h=25,txt= self.seat_number,border=1,lu=1)
            
            #price row
            pdf.set_font(family = "Times",style="B",size=14)
            pdf.cell(w=100,h=25,txt="price: ",border=1)
            pdf.set_font(family = "Times",style="B",size=12)
            pdf.cell(w=0,h=25,txt= f"{self.price}",border=1,lu=1)
        
            pdf.output("cinema.pdf","F")

if __name__ == '__main__':
    name = input("your full name: ")
    seat_id = input("prefered seat number: ")
    card_type = input("your card type: ")
    card_number = input("your card number: ")
    card_cvc = input("card cvc: ")
    card_holder = input("card holder name: ")
    
    user = User(name)
    seat = Seat(seat_id)
    card = Card(card_type,card_number,card_cvc,card_holder)

    print(user.buy(seat,card))
    # pdf = FPDF(orientation = "p", unit = "pt", format="A4")
    # pdf.add_page()
            
    # pdf.set_font(family = 'times', style= 'B',size=24)
    # pdf.cell(w=0, h=80,txt="CPL DIgital Ticket",border= 1,ln=1, align="C")
    # pdf.output("Test-PDF.pdf","F")











import pandas as pd

data = pd.read_csv('hotels.csv', dtype={'id':str})

class Hotel:
    def __init__(self, hotelid):
        self.the_hotel_id = hotelid
        self.name = data.loc[data['id'] == self.the_hotel_id, 'name'].squeeze()
        self.hotel_capacity = data.loc[data['id'] == self.the_hotel_id, 'capacity'].squeeze()

    def available(self):
        """Checks if the Hotel is available"""
        availability_status = data.loc[data['id'] == self.the_hotel_id]['available'].squeeze()
        if availability_status == 'yes':
            return 'Hotel is Available!'
        else:
            return 'Hotel is not available! Try again next time!'

    def book(self):
        """Checks the Availability of the Hotels and changing it no 'no' if they are booked"""
        avail = data.loc[data['id'] == self.the_hotel_id]['available'].squeeze()
        if avail == 'yes':
            avail = avail.replace('yes','no')
        data.to_csv('hotels.csv', index=False)
        return 'Hotel Booked!'

    def capacity(self):
        return self.hotel_capacity

class ReservationTicket():
    def __init__(self, name, hotel):
        self.customer_name = name
        self.hotel_object = hotel

    def generate_ticket(self):
        content = f"""
        Thank you for your service at WorstHotels.com!
        Name: {self.customer_name}
        Hotel Name: {self.hotel_object.name}
        Customer Email: fatphobic@gigachad.com
        Customer Number: 6942042069
        Reservation Status: BOOKED
        Reservation ID: 42851HTF248 
        
        Scan the Below QR Code for Exciting Add-Ons and Discount Coupons
        
                            AGDSFHGDFHADHF
                            436364G3Q4V34G
                            3Q4643Q6346T34
                            H46Y5;]A[GK[ER
                            SD';LFK43[OER'
                            5Y34T304T43T63
        """
        return content

# name
# city
# capacity
# available
# id
print(data)
hotel_id = input('Enter Hotel ID: ')
hotel = Hotel(hotel_id)


if hotel.available():
    print(f'Capacity of your Hotel is {hotel.capacity()} persons.')
    print('Hotel is Available!')
    hotel.book()
    name = input('Enter Your Name: ')
    ticket = ReservationTicket(name, hotel)
    print(ticket.generate_ticket())


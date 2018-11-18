from api.models.models import Parcel, User
from api.models.dbconnection import Dbcontroller
class ParcelDb(Dbcontroller):

    def __init__(self):
        super().__init__()

    def add_parcel(self,parcel):
        self.cursor.execute("INSERT INTO parcels(parcel_name,price,\
        parcel_status,usrId,parcel_source,parcel_destination,present_location)\
        VALUES(%s, %s, %s, %s, %s, %s, %s);",(parcel.name,parcel.price,\
        parcel.status,parcel.id,parcel.source,parcel.destination,parcel.location))

    def fetch_all_orders(self):
        return self.fetch_all_entries('parcels')

    def fetch_parcel(self,id):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM parcels WHERE parcelid=%s"
        self.cursor.execute(query, (id,))
        parcel = self.cursor.fetchone()
        return parcel

    def fetch_parcel_by_specific(self,id):
        """Returns a user in form of a dict or None if user not found"""
        query = "SELECT * FROM parcels WHERE usrid=%s"
        self.cursor.execute(query, (id,))
        parcels = self.cursor.fetchall()
        return parcels

import peewee
import base
from place import Place
from amenity import Amenity


class PlaceAmenities(peewee.Model):
    place = ForeignKeyField(Place)
    amenity = ForeignKeyField(Amenity)

    class Meta:
        database = database

#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel
from models.base_model import BaseModel, Base
from sqlalchemy import (Column, String,
                        ForeignKey, Float,
                        Integer)
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    places = relationship("Review", backref="place", cascade="all, delete-orphan")
    amenity_ids = []


    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def reviews(self):
            """ 
            review
            """
            all_reviews = list(models.storage.all(Review).values())

            review_list = [r for r in all_reviews if r.place_id == self.id]
            return review_list
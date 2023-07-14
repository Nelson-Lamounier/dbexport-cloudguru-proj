from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, Boolean, TIMES TAMP, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Product():
    __tablename__= "products"

    id = Column(Integer, primary_key=True)
    name = Column(Integer, nullable=False)
    published = Column(Boolean, nullable=False)
    created_on = Column(TIMESTAMP)

    # Defining model relationships
    reviews = relationship("Review", order_by="Review.rating", back_populates="product")

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeighKey("products.id"))
    rating = Column(Integer, nullable= False)
    comment = Column(Text)
    created_on = Column(TIMESTAMP)

    # Defining model relationships
    product = relationship("Product", back_populates="reviews")

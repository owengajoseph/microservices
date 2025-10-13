from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db import Model
from sqlalchemy import ForeignKey
from typing import Optional
from sqlalchemy import Table, Column

# # this is a model as the name suggests it models the database
# # this will be used by the database referenced by engine to create tables
# # engine here stands for the database im im using eg postgres, sql
# class Product(Model):
#     __tablename__ = "products"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(64))
#     manufacturer: Mapped[str] = mapped_column(String(64))
#     year: Mapped[int]
#     country: Mapped[str] = mapped_column(String(32))
#     cpu: Mapped[str] = mapped_column(String(32))

#     def __repr__(self):
#         return f'Product({self.id}, "{self.name}")'


# class Product(Model):
#     __tablename__ = "products"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
#     manufacturer_id: Mapped[int] = mapped_column(
#         ForeignKey("manufacturers.id"), index=True
#     )
#     year: Mapped[int] = mapped_column(index=True)
#     country: Mapped[Optional[str]] = mapped_column(String(32))
#     cpu: Mapped[Optional[str]] = mapped_column(String(32))
#     manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")

#     def __repr__(self):
#         return f'Product({self.id}, "{self.name}")'

ProductCountry = Table(
    "products_countries",
    Model.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True, nullable=False),
    Column("country_id", ForeignKey("countries.id"), primary_key=True, nullable=False),
)


class Product(Model):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    manufacturer_id: Mapped[int] = mapped_column(
        ForeignKey("manufacturers.id"), index=True
    )
    year: Mapped[int] = mapped_column(index=True)
    cpu: Mapped[Optional[str]] = mapped_column(String(32))
    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")
    countries: Mapped[list["Country"]] = relationship(
        secondary=ProductCountry, back_populates="products"
    )

    def __repr__(self):
        return f'Product({self.id}, "{self.name}")'


class Country(Model):
    __tablename__ = "countries"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32), index=True, unique=True)
    products: Mapped[list["Product"]] = relationship(
        secondary=ProductCountry, back_populates="countries"
    )

    def __repr__(self):
        return f'Country({self.id}, "{self.name}")'


# x = Country(id=1, name="foo", products=[""])


class Manufacturer(Model):
    products: Mapped[list["Product"]] = relationship(
        cascade="all, delete-orphan", back_populates="manufacturer"
    )
    __tablename__ = "manufacturers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(64), index=True, unique=True)

    def __repr__(self):
        return f'Manufacturer({self.id}, "{self.name}")'

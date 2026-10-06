"""
Test Factory to make fake objects for testing
"""
import factory
from factory import Sequence, Faker
from factory.alchemy import SQLAlchemyModelFactory
from service.models import db, Product, Category


class ProductFactory(SQLAlchemyModelFactory):
    """Creates fake products for testing"""

    class Meta:
        model = Product
        sqlalchemy_session = db.session

    id = Sequence(lambda n: n)
    name = Faker("first_name")
    description = Faker("sentence")
    price = Faker("pydecimal", left_digits=6, right_digits=2, positive=True)
    available = Faker("pybool")
    category = Faker(
        "random_element",
        elements=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ],
    )

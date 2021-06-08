from typing import cast
from flask_sqlalchemy import SQLAlchemy
from typings.sql_alchemy import SQLAlchemy as SQLAlchemyStub


db: SQLAlchemyStub = cast(SQLAlchemyStub, SQLAlchemy())

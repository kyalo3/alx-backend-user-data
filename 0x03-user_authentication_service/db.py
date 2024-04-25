#!/usr/bin/env python3

"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()

        """returns a session object"""
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ The method should save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        """returns a User object"""
        return user

    def find_user_by(self, **kwargs):
        """ Return the first row found in the users table
        """
        if not kwargs:
            InvalidRequestError
        if not all()
        try:
            return self._session.query(User).filter_by(**kwargs).first()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise

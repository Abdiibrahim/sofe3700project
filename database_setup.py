from sqlalchemy import Column, ForeignKey, INTEGER, VARCHAR, CHAR, String, BOOLEAN, DATE
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Vehicles(Base):
    __tablename__ = 'vehicles'

    lplate = Column(VARCHAR(50))
    province = Column(VARCHAR(50))
    vehicleid = Column(VARCHAR(4), primary_key=True)
    make = Column(VARCHAR(50))
    model = Column(VARCHAR(50))
    year = Column(INTEGER)
    colour = Column(VARCHAR(50))

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return {
            'lplate': self.lplate,
            'province': self.province,
            'vid': self.vid,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'colour': self.colour,
        }


class Crashes(Base):
    __tablename__ = 'crashes'

    crashno = Column(INTEGER, primary_key=True)
    location = Column(VARCHAR(50))
    crashdate = Column(DATE)
    crashtime = Column(VARCHAR(50))
    crashcause = Column(String)
    crashcity = Column(VARCHAR(50))
    crashprovince = Column(VARCHAR(50))

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return {
            'crashno': self.crashno,
            'location': self.location,
            'crashdate': self.crashdate,
            'crashtime': self.crashtime,
            'crashcause': self.crashcause,
        }


class Victims(Base):
    __tablename__ = 'victims'

    victimid = Column(INTEGER, primary_key=True)
    fname = Column(VARCHAR(50))
    lname = Column(VARCHAR(50))
    dob = Column(DATE)
    gender = Column(CHAR(1))
    city = Column(VARCHAR(50))
    province = Column(VARCHAR(50))
    vehicleid = Column(VARCHAR(4), ForeignKey('vehicles.vehicleid'))
    crashno = Column(INTEGER, ForeignKey('crashes.crashno'))
    vehicles = relationship(Vehicles)
    crashes = relationship(Crashes)

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return {
            'victimid': self.victimid,
            'fname': self.fname,
            'lname': self.lname,
            'dob': self.dob,
            'gender': self.gender,
            'city': self.city,
            'province': self.province,
            'vehicleid': self.vehicleid,
            'crashno': self.crashno,
        }


class Injuries(Base):
    __tablename__ = 'injuries'

    crashno = Column(INTEGER, ForeignKey('crashes.crashno'), primary_key=True)
    victimid = Column(INTEGER, ForeignKey('victims.victimid'), primary_key=True)
    injurytype = Column(VARCHAR(50))
    fatality = Column(BOOLEAN)
    driver = Column(BOOLEAN)
    crashes = relationship(Crashes)
    victims = relationship(Victims)

    @property
    def serialize(self):
        # Return object data in easily serializable format
        return {
            'crashno': self.crashno,
            'victimid': self.victimid,
            'injurytype': self.injurytype,
            'fatality': self.fatality,
            'driver': self.driver,
        }


engine = create_engine('sqlite:///crashproject.db')
Base.metadata.create_all(engine)

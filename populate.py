from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Victims, Vehicles, Base, Crashes, Injuries
import datetime

# open 'crashproject.db' and create engine
engine = create_engine('sqlite:///crashproject.db')
Base.metadata.bind = engine

# start a session with the database
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add tuples for the crashes into the database
# Data for crash1
vehicle1 = Vehicles(lplate='ARF 5975', province='ON', vehicleid='C25D', make='GMC', model='Sierra',
                    year=2005, colour='White')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='GMC 4857', province='ON', vehicleid='F709', make='Mercedes', model='CLA45',
                    year=2015, colour='White')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2001, location='rural roads', crashdate=datetime.date(2017, 1, 1), crashtime='Morning',
                crashcause='wet road', crashcity='Pickering', crashprovince='ON', crashlat=43.8384, crashlng=-79.0868)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1006, fname='Tom', lname='Wilson', dob=datetime.date(1992, 5, 7), gender='M', city='Whitby',
                  province='ON', vehicleid='C25D', crashno=2001)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1012, fname='Kate', lname='Spade', dob=datetime.date(1990, 7, 19), gender='F', city='Mississauga',
                  province='ON', vehicleid='F709', crashno=2001)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2001, victimid=1006, injurytype='Head', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2001, victimid=1012, injurytype='Arm', fatality=False, driver=True)
session.add(injury2)
session.commit()


# Data for crash2
vehicle1 = Vehicles(lplate='RRR 8074', province='ON', vehicleid='CRC1', make='Nissan', model='240SX',
                    year=1998, colour='Green')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='FOP 7303', province='ON', vehicleid='D158', make='GMC', model='Terrain',
                    year=2016, colour='Silver')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2002, location='highway', crashdate=datetime.date(2016, 2, 15), crashtime='Night', 
				crashcause='Speed', crashcity='Kitchener', crashprovince='ON', crashlat=43.4503, crashlng=-80.4832)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1005, fname='Reid', lname='Stevens', dob=datetime.date(1993, 1, 1), gender='M', city='London',
                  province='ON', vehicleid='CRC1', crashno=2002)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1007, fname='Kevin', lname='Spacey', dob=datetime.date(1991, 9, 9), gender='M', city='Bowmanville',
                  province='ON', vehicleid='D158', crashno=2002)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2002, victimid=1005, injurytype='Arm', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2002, victimid=1007, injurytype='Leg', fatality=False, driver=True)
session.add(injury2)
session.commit()


# Data for crash3
vehicle1 = Vehicles(lplate='BBS 3003', province='ON', vehicleid='B9R5', make='Toyota', model='Camry', year=2010,
                    colour='Grey')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='NYR 5321', province='ON', vehicleid='EE1F', make='Toyota', model='Corolla', year=2000,
                    colour='Blue')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2003, location='highway', crashdate=datetime.date(2017, 12, 1), crashtime='Afternoon', 
				crashcause='Snow', crashcity='Markham', crashprovince='ON', crashlat=43.8561, crashlng=-79.3370)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1003, fname='Steven', lname='Pavlatos', dob=datetime.date(1997, 9, 17), gender='M', city='Markham',
                  province='ON', vehicleid='B9R5', crashno=2003)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1009, fname='Sandra', lname='Borque', dob=datetime.date(1974, 12, 13), gender='F', city='Toronto',
                  province='ON', vehicleid='EE1F', crashno=2003)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2003, victimid=1003, injurytype='Leg', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2003, victimid=1009, injurytype='Neck', fatality=False, driver=True)
session.add(injury2)
session.commit()


# Data for crash4
vehicle1 = Vehicles(lplate='WKK 4399', province='ON', vehicleid='A74C', make='Ford', model='Focus', year=2013,
                    colour='Black')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='JFX 2214', province='ON', vehicleid='D9C2', make='Honda', model='S2000', year=2003,
                    colour='White')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2004, location='residential', crashdate=datetime.date(2016, 11, 12), crashtime='Afternoon',
                crashcause='Distracted', crashcity='Hamilton', crashprovince='ON', crashlat=43.2557, crashlng=-79.8711)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1002, fname='Abdi', lname='Ibrahim', dob=datetime.date(1997, 6, 13), gender='M', city='Hamilton',
                  province='ON', vehicleid='A74C', crashno=2004)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1008, fname='Ashley', lname='Sumed', dob=datetime.date(1999, 11, 11), gender='F', city='Scarborough',
                  province='ON', vehicleid='D9C2', crashno=2004)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2004, victimid=1002, injurytype='Neck', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2004, victimid=1008, injurytype='Neck', fatality=False, driver=True)
session.add(injury2)
session.commit()


# Data for crash5
vehicle1 = Vehicles(lplate='MRS 7137', province='ON', vehicleid='E296', make='Nissan', model='Rouge', year=2009,
                    colour='Grey')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='SPA 0134', province='ON', vehicleid='F211', make='Ford', model='F150', year=2016,
                    colour='Red')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2005, location='highway', crashdate=datetime.date(2015, 5, 10), crashtime='Night',
                crashcause='Following too closely', crashcity='Kingston', crashprovince='ON', crashlat=44.2312, crashlng=-76.4860)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1010, fname='Stacy', lname='Mann', dob=datetime.date(2000, 3, 15), gender='F', city='Ottawa',
                  province='ON', vehicleid='E296', crashno=2005)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1011, fname='Lisa', lname='Inler', dob=datetime.date(1987, 5, 17), gender='F', city='Ajax',
                  province='ON', vehicleid='F211', crashno=2005)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2005, victimid=1010, injurytype='Back', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2005, victimid=1011, injurytype='Head', fatality=True, driver=True)
session.add(injury2)
session.commit()


# Data for crash6
vehicle1 = Vehicles(lplate='ZMT 1193', province='ON', vehicleid='A15D', make='Honda', model='CRV', year=2015,
                    colour='silver')
session.add(vehicle1)
session.commit()

vehicle2 = Vehicles(lplate='CNN 0504', province='ON', vehicleid='B2C6', make='Chevrolet', model='Equinox', year=2017,
                    colour='Black')
session.add(vehicle2)
session.commit()

crash = Crashes(crashno=2006, location='intersection', crashdate=datetime.date(2010, 4, 18), crashtime='Morning',
                crashcause='Ran red light', crashcity='Oshawa', crashprovince='ON', crashlat=43.8971, crashlng=-78.8658)
session.add(crash)
session.commit()

victim1 = Victims(victimid=1001, fname='Prasheel', lname='Bhagalia', dob=datetime.date(1997, 3, 22), gender='M', city='Brampton',
                  province='ON', vehicleid='A15D', crashno=2006)
session.add(victim1)
session.commit()

victim2 = Victims(victimid=1004, fname='Austin', lname='McCulloch', dob=datetime.date(1997, 9, 23), gender='M', city='Oshawa',
                  province='ON', vehicleid='B2C6', crashno=2006)
session.add(victim2)
session.commit()

injury1 = Injuries(crashno=2006, victimid=1001, injurytype='Back', fatality=False, driver=True)
session.add(injury1)
session.commit()

injury2 = Injuries(crashno=2006, victimid=1004, injurytype='Leg', fatality=False, driver=True)
session.add(injury2)
session.commit()


print "added crash data!"

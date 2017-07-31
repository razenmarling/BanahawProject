from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, func, Date
from decimal import Decimal
import datetime
import uuid

Base = declarative_base()

class GenericBase(object):

    def as_dict(self):
        return ({c.name: getattr(self, c.name) for c in self.__table__.columns})

    def toJSONExcept(self,*except_fields):
        retval = {}
        tabledic = self.as_dict()
        for k in tabledic:
            if k in except_fields:
                continue

            if type(tabledic[k]) in [datetime.datetime,datetime.date]:
                tabledic[k] = tabledic[k].strftime('%m/%d/%Y %H:%M')
            elif type(tabledic[k]) is Decimal:
                tabledic[k] = float(tabledic[k])
            elif type(tabledic[k]) is uuid.UUID:
            	tabledic[k] = str(tabledic[k])

            retval[k] = tabledic[k]

        return retval

class Users_table(GenericBase,Base):
	__tablename__ = 'users'

	userid = Column(Integer,primary_key=True)
	username = Column(String(50))
	password = Column(String(50))
	role = Column(String(50))


class T_Regular_Services(GenericBase,Base):
    __tablename__ = 'regular_services'

    regular_services_id = Column(Integer,primary_key=True)
    service_name = Column(Integer)
    off_peak_price = Column(Integer)
    peak_price = Column(Integer)
    non_member_price = Column(Integer)
    duration = Column(Integer)
    datecreated = Column(Date, default=datetime.datetime.now())


class T_Healing_Packages(GenericBase,Base):
    __tablename__ = 'healing_packages'

    healing_packages_id = Column(Integer,primary_key=True)
    package_name = Column(Integer)
    member_price = Column(Integer)
    non_member_price = Column(Integer)
    duration = Column(Integer)
    datecreated = Column(Date, default=datetime.datetime.now())

class T_Facial_Services(GenericBase,Base):
    __tablename__ = 'facial_services'

    facial_services_id = Column(Integer,primary_key=True)
    facial_services_name = Column(Integer)
    member_price = Column(Integer)
    non_member_price = Column(Integer)
    duration = Column(Integer)
    datecreated = Column(Date, default=datetime.datetime.now())


class T_Add_Ons(GenericBase,Base):
    __tablename__ = 'add_ons'

    add_ons_id = Column(Integer,primary_key=True)
    add_ons_name = Column(Integer)
    member_price = Column(Integer)
    non_member_price = Column(Integer)
    duration = Column(Integer)
    datecreated = Column(Date, default=datetime.datetime.now())


class T_Branch(GenericBase,Base):
    __tablename__ = 'branch'

    branchid = Column(Integer,primary_key=True)
    branch_name = Column(String(50))


class T_Attendants(GenericBase,Base):
    __tablename__ = 'attendant'

    attendantid = Column(Integer,primary_key=True)
    attendant_name = Column(String(50))
    allowance = Column(Integer)
    hiredate = Column(String(50))
    mobilenumber = Column(String(20))
    position = Column(String(50))
    address = Column(String(100))
    datecreated = Column(Date, default=datetime.datetime.now())

class T_Attendants01(GenericBase,Base):
    __tablename__ = 'attendant01'

    attendant01id = Column(Integer,primary_key=True)
    attendantid = Column(Integer)
    timein = Column(String(10))
    timeout = Column(String(10))
    trandate = Column(Date, default=datetime.datetime.now().date())

class T_Member00(GenericBase,Base):
    __tablename__ = 'member00'

    member00id = Column(Integer,primary_key=True)
    name = Column(String(50))
    address = Column(String(50))
    mobile_number = Column(String(50))
    landline_number = Column(String(50))
    email_address = Column(String(50))
    birthdate = Column(String(50))
    membertype = Column(String(50))
    feedback = Column(String(100))
    membershipcost = Column(Integer)
    datecreated = Column(Date, default=datetime.datetime.now().date())
    attendant_name = Column(String(50))
    attendantid = Column(Integer)
    upgraded = Column(Date)
    upgraded_by = Column(Integer)
    branch = Column(String(50))


class T_Member01(GenericBase,Base):
    __tablename__ = 'member01'

    member01id = Column(Integer, primary_key=True)
    member00id = Column(Integer, ForeignKey(T_Member00.member00id))
    name = Column(String(50))
    relationship = Column(String(50))
    datecreated = Column(DateTime, default = func.now())


class T_Transaction(GenericBase,Base):
    __tablename__ = 'transactions'

    transactionid = Column(Integer, primary_key=True)
    transaction_type = Column(String(20))
    client_name = Column(String(50))
    member00id = Column(Integer)
    client_type = Column(String(50))
    branch = Column(String(50))
    service_type = Column(String(50))
    service = Column(String(50))
    add_ons = Column(String(50))
    products = Column(String(50))
    attendant_name = Column(String(50))
    attendantid = Column(Integer)
    estimated_time = Column(Integer)
    time_spent = Column(Integer)
    total_amount = Column(Integer)
    payment_type = Column(String(50))
    service_price = Column(Integer)
    add_ons_price = Column(String(255))
    active = Column(Boolean)
    datestart = Column(DateTime, default=func.now())
    dateend = Column(DateTime)
    datecreated = Column(Date, default=datetime.datetime.now().date())


class T_Reservation(GenericBase,Base):
    __tablename__ = 'reservations'

    reservationid = Column(Integer, primary_key=True)
    transaction_type = Column(String(20))
    client_name = Column(String(50))
    member00id = Column(Integer)
    client_type = Column(String(50))
    branch = Column(String(50))
    service_type = Column(String(50))
    service = Column(String(50))
    add_ons = Column(String(50))
    products = Column(String(50))
    attendant_name = Column(String(50))
    attendantid = Column(Integer)
    estimated_time = Column(Integer)
    time_spent = Column(Integer)
    total_amount = Column(Integer)
    service_price = Column(Integer)
    add_ons_price = Column(String(255))
    payment_type = Column(String(50))
    active = Column(Boolean)
    datestart = Column(DateTime)
    dateend = Column(DateTime)
    datecreated = Column(Date, default=datetime.datetime.now().date())
    res_date = Column(Date)
    res_time = Column(String(50))


class T_Products(GenericBase, Base):
    __tablename__ = 'products'

    productid = Column(Integer, primary_key=True)
    productname = Column(String(100))
    amountpaid = Column(Integer)
    datepurchased = Column(Date, default=datetime.datetime.now().date())

class T_promos(GenericBase, Base):
    __tablename__ = 'promos'

    promoid = Column(Integer, primary_key=True)
    description = Column(String(100))
    member_price = Column(Integer)
    non_member_price = Column(Integer)
    duration = Column(Integer)
    datestart = Column(Date)
    dateend = Column(Date)
    active = Column(Boolean)

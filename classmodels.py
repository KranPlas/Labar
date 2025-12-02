from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from datetime import datetime


engine = create_engine('sqlite:///labar.db', pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)
session = Session()

class Programs(Base):
    __tablename__ = 'Programs'
    software_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    version = Column(String(50))
    release_date = Column(String(50))
    developer = Column(String(50))
    category = Column(String(50))


class PCs(Base):
    __tablename__ = 'PCs'
    pc_id = Column(Integer, primary_key=True)
    program = Column(String(50))
    user = Column(String(50))
    name = Column(String(50))
    inst_place = Column(String(50))

class Users(Base):
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    role = Column(String(50))
    created_at = Column(String(100))


class PCs_CRUD:
    @staticmethod
    def print_rec_pc():
        return session.query(PCs).all()

    @staticmethod
    def print_rec_id_pc(pc_id):
        return session.query(PCs).filter(PCs.pc_id == pc_id).first()

    @staticmethod
    def create_rec_pc(name, program, user, inst_place):
        computer = PCs(name=name, program=program, user=user, inst_place=inst_place)
        session.add(computer)
        session.commit()
        return computer

    @staticmethod
    def del_rec(computer_id):
        computer = PCs_CRUD.print_rec_id_pc(computer_id)
        if computer:
            session.delete(computer)
            session.commit()



class Users_CRUD:
    @staticmethod
    def print_rec_user():
        return session.query(Users).all()

    @staticmethod
    def print_rec_id_user(user_id):
        return session.query(Users).filter(Users.user_id == user_id).first()

    @staticmethod
    def create_rec_user(name, email, role):
        user = Users(name=name, email=email, role=role, created_at=datetime.now())
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def del_rec_user(user_id):
        user = Users_CRUD.print_rec_id_user(user_id)
        if user:
            session.delete(user)
            session.commit()


class Programs_CRUD:
    @staticmethod
    def print_rec_prog():
        return session.query(Programs).all()

    @staticmethod
    def print_rec_id_prog(software_id):
        return session.query(Programs).filter(Programs.software_id == software_id).first()

    @staticmethod
    def create_rec_prog(name, version, date_release, developer, category):
        program = Programs(name=name, vesion=version, date_release=date_release, developer=developer, category=category)
        session.add(program)
        return program

    @staticmethod
    def del_rec_prog(software_id):
        program = Programs.print_rec_id_prog(software_id)
        if program:
            session.delete(program)
            session.commit()

with session as session:

    new_user = Users_CRUD.create_rec_user("You", 'youremail@mail.com', "user")
    print('Добавлен новый пользователь!')
    print(f"Данные пользователя \n Id: {new_user.user_id} \n Name: {new_user.name} \n Email: {new_user.email} \n Role: {new_user.role}")

    print('\n===all pcs===\n')
    computers = PCs_CRUD.print_rec_pc()
    for comp in computers:
        print(f"Id: {comp.pc_id}, {comp.program}, {comp.user}, {comp.name}")

    print('\n===all users===\n')
    users = Users_CRUD.print_rec_user()
    for us in users:
        print(f"Id: {us.user_id}, {us.name}, {us.email}, {us.role}, {us.created_at}")

    print('\n===all programs===\n')
    programs = Programs_CRUD.print_rec_prog()
    for prog in programs:
        print(f"Id: {prog.software_id}, {prog.name}, {prog.version}, {prog.developer}, {prog.category}")

    Users_CRUD.del_rec_user(4)
    print('\nУдален пользователь!')

    print('\n===all users===\n')
    users = Users_CRUD.print_rec_user()
    for us in users:
        print(f"Id: {us.user_id}, {us.name}, {us.email}, {us.role}, {us.created_at}")

    session.close()
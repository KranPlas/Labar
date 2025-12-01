from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.sql.functions import user
from datetime import datetime

# Подключение к существующей базе
engine = create_engine('sqlite:///labar.db', pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

Session = sessionmaker(bind=engine)
session = Session()

class Programs(Base): #Классы-модель
    __tablename__ = 'Programs'
    software_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    version = Column(String(50))
    release_date = Column(String(50))
    developer = Column(String(50))
    category = Column(String(50))


class PCs(Base): #Класс-модель
    __tablename__ = 'PCs'
    pc_id = Column(Integer, primary_key=True)
    program = Column(String(50))
    name = Column(String(50))
    inst_place = Column(String(50))

class Users(Base): #Класс-модель
    __tablename__ = 'Users'
    user_id = Column(Integer, primary_key=True)
    pc = Column(String(50))
    name = Column(String(50))
    email = Column(String(50))
    role = Column(String(50))
    created_at = Column(String(50))


#CRUD
class PCs_CRUD:
    @staticmethod
    def print_rec_pc(): #функция для получения всех записей в таблице компьютеров
        return session.query(PCs).all()

    @staticmethod
    def print_rec_id_pc(pc_id): #найти запись по айди в таблице с компьютерами
        return session.query(PCs).filter(PCs.pc_id == pc_id).first()

    @staticmethod
    def create_rec(name, program, inst_place): #добавить компьютер в бд
        computer = PCs(name=name, program=program, inst_place=inst_place)
        session.add(computer)
        session.commit()
        return computer

    @staticmethod
    def del_rec(computer_id): #удалить компьютер из бд
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
    def create_rec(name, pc, email, role): #добавить компьютер в бд
        user = Users(name=name, pc=pc , email=email, role=role, created_at=datetime.now())
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def del_rec_user(user_id):
        user = PCs_CRUD.print_rec_id_pc(user_id)
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


#Сервис, чтобы работать со связ-ми данными из неск-х таблиц
class work_with_tables:
    @staticmethod
    def join_sql():
        return session.query(
            PCs.pc_id, PCs.name, Programs.name).join(
            Programs, PCs.program == Programs.software_id)

    @staticmethod
    def find_prog_on_pc(name_program): #для нахождения компьютера с определенным по
        return session.query(PCs).join(Programs).filter(Programs.software_id == name_program).all()

with session as session:
    print('all pcs')
    computers = PCs_CRUD.print_rec_pc()
    #for comp in computers:
     #   print(f"Id: {comp.pc_id}, {comp.program}, {comp.name}")

#краш-тест
'''
if __name__ == "__main__":
    print("Все компьютеры ")
    computers = ComputerCRUID.records() #да-да та самая функция, которая выводит вапще всё
    for comp in computers:
        print(f"ID: {comp.id_pc}, Email: {comp.Email}, PO ID: {comp.id_proga}")

    new_comp = ComputerCRUID.createrecord("crashtest@example.com", 1) #внедряю тестовую запись
    print(f"\nДобавлен компьютер с ID: {new_comp.id_pc}")
    ComputerCRUID.change_email(new_comp.id_pc, "crashtestnew@example.com")#а затем обновляю её


    print("\nВся таблица")
    resultat = ServiceTableData.join_sql()
    print("ID | Почта | ПО | Цена")
    for id_pc, email, proga, price in resultat:
        print(f"{id_pc} | {email} | {proga} | {price}")

    print("\nВывод пк с visual studio (для теста)")
    vs_pc = ServiceTableData.find_pc_po("Visual Studio")
    for j in vs_pc:
        print(f"ID: {j.id_pc}, Email: {j.Email}")

    ComputerCRUID.deleterecord(new_comp.id_pc) #тестовый компьютер пака(удаляю)
    print(f"\nУдален компьютер с ID: {new_comp.id_pc}")

    session.close()
'''
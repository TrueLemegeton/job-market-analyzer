from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass


class Vacancy(Base):
    __tablename__ = 'vacancies'

    hh_id: Mapped[int | None] = mapped_column(unique=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    company: Mapped[str | None] = mapped_column()
    employment: Mapped[str | None] = mapped_column()
    link: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str] = mapped_column()
    address: Mapped[str | None] = mapped_column()
    payment_frequency: Mapped[str | None] = mapped_column()
    collected_at: Mapped[datetime] = mapped_column()

    salary_from: Mapped[int | None] = mapped_column()
    salary_to: Mapped[int | None] = mapped_column()
    salary_currency: Mapped[str | None] = mapped_column()
    salary_period: Mapped[str | None] = mapped_column()
    tax_status: Mapped[str | None] = mapped_column()

    experience_from: Mapped[int | None] = mapped_column()
    experience_to: Mapped[int | None] = mapped_column()

    is_active: Mapped[bool] = mapped_column(default=True)
    has_other_options: Mapped[bool] = mapped_column()
    by_agreement: Mapped[bool] = mapped_column()
    has_night_shifts: Mapped[bool] = mapped_column()


    skills: Mapped[list['Skill']] = relationship(secondary='vacancy_skills', back_populates='vacancies')
    schedules: Mapped[list['Schedule']] = relationship(secondary='vacancy_schedules', back_populates='vacancies')
    work_formats: Mapped[list['WorkFormat']] = relationship(secondary='vacancy_work_formats', back_populates='vacancies')
    working_hours: Mapped[list['WorkingHours']] = relationship(secondary='vacancy_working_hours', back_populates='vacancies')
    hiring_formats: Mapped[list['HiringFormat']] = relationship(secondary='vacancy_hiring_formats', back_populates='vacancies')


# ------------------ #
class Skill(Base):
    __tablename__ = 'skills'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    vacancies: Mapped[list['Vacancy']] = relationship(secondary='vacancy_skills', back_populates='skills')

class VacancySkill(Base):
    __tablename__ = 'vacancy_skills'

    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), primary_key=True)
    skill_id: Mapped[int] = mapped_column(ForeignKey('skills.id'), primary_key=True)
# ------------------ #


# ------------------ #
class Schedule(Base):
    __tablename__ = 'schedules'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    vacancies: Mapped[list['Vacancy']] = relationship(secondary='vacancy_schedules', back_populates='schedules')


class VacancySchedule(Base):
    __tablename__ = 'vacancy_schedules'

    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), primary_key=True)
    schedule_id: Mapped[int] = mapped_column(ForeignKey('schedules.id'), primary_key=True)
# ------------------ #


# ------------------ #
class WorkFormat(Base):
    __tablename__ = 'work_formats'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    vacancies: Mapped[list['Vacancy']] = relationship(secondary='vacancy_work_formats', back_populates='work_formats')

class VacancyWorkFormat(Base):
    __tablename__ = 'vacancy_work_formats'

    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), primary_key=True)
    work_format_id: Mapped[int] = mapped_column(ForeignKey('work_formats.id'), primary_key=True)
# ------------------ #


# ------------------ #
class WorkingHours(Base):
    __tablename__ = 'working_hours'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    vacancies: Mapped[list['Vacancy']] = relationship(secondary='vacancy_working_hours', back_populates='working_hours')

class VacancyWorkingHours(Base):
    __tablename__ = 'vacancy_working_hours'

    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), primary_key=True)
    working_hour_id: Mapped[int] = mapped_column(ForeignKey('working_hours.id'), primary_key=True)
# ------------------ #


# ------------------ #
class HiringFormat(Base):
    __tablename__ = 'hiring_formats'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    vacancies: Mapped[list['Vacancy']] = relationship(secondary='vacancy_hiring_formats', back_populates='hiring_formats')

class VacancyHiringFormat(Base):
    __tablename__ = 'vacancy_hiring_formats'

    vacancy_id: Mapped[int] = mapped_column(ForeignKey('vacancies.id'), primary_key=True)
    hiring_format_id: Mapped[int] = mapped_column(ForeignKey('hiring_formats.id'), primary_key=True)
# ------------------ #
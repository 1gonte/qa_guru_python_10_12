import dataclasses


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subject: str
    hobby: str
    photo_name: str
    current_address: str
    state: str
    city: str


student = Users(
    first_name='Georgii',
    last_name='Sergeev',
    email='example@gmail.com',
    gender='Male',
    mobile_number='0123456789',
    year_of_birth='2001',
    month_of_birth='February',
    day_of_birth='16',
    subject='Computer Science',
    hobby='Reading',
    photo_name='image.png',
    current_address='Moscow, Red Square, 1A',
    state='NCR',
    city='Delhi')
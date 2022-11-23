import datetime
from typing import List


class RoadArea:

    def __init__(self, rating: int, coordinates: int):
        self.rating = rating
        self.coordinates = coordinates

    def add_road_work(self):
        pass

    def del_road_work(self):
        pass

    def add_road_accident(self):
        pass

    def add_feedback(self, description: str, mark: int):
        pass


class RoadAccident:
    def __init__(self, status: bool):
        self.status = status


class Request:
    def __init__(self, place: RoadArea, description: str, status: bool):
        self.place = place
        self.status = status
        self.date = datetime.date.today()
        self.description = description


class RoadWork:
    def __init__(self, req: Request, status):
        self.request = req
        self.status = status


class Controller:

    def registration(self):
        pass

    def authorization(self):
        pass


class AppUser:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def view_feedbacks(self, area: RoadArea):
        pass

    def view_roads(self):
        pass


class UserInspector(AppUser):

    def add_record_road_work(self, area: RoadArea, req: Request):
        pass

    def del_road_work(self, work: RoadWork):
        pass

    def view_requests(self):
        pass


class UserDriver(AppUser):

    def __init__(self, phone: int):
        self.phone = phone

    def add_request(self, area: RoadArea, description: str):
        pass

    def add_feedback(self, area: RoadArea, feedback: str, rate: int):
        pass

    def add_road_accident(self, area: RoadArea):
        pass


class Comment:
    def __init__(self, author: UserDriver, description: str, mark: int):
        self.author = author
        self.description = description
        self.mark = mark


class RoadService:
    def __init__(self, user: AppUser, codes: List[str]):
        self.user = user
        self.codes = codes

    def registration_driver(self, tel: int, log: str, passwd: str):
        pass

    def registration_inspector(self, log: str, passwd: str):
        pass

    def authorization(self, log: str, psswd: str):
        pass

    def add_road_work(self, area: RoadArea, req: Request):
        pass

    def del_road_work(self, work: RoadWork):
        pass

    def add_road_accident(self, area: RoadAccident):
        pass

    def add_request(self, req: Request):
        pass

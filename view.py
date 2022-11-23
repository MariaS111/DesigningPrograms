from kivy.config import Config

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from system import *
from kivy.core.window import Window

Builder.load_file("ui.kv")


class SignInScreen(Screen):
    def authorization(self, log, passwd):
        RoadService.authorization(RoadService, log, passwd)


class SignUpUScreen(Screen):
    def register_user(self, log, tel, passwd):
        RoadService.registration_driver(RoadService, log, tel, passwd)


class SignUpIScreen(Screen):
    def register_ins(self, log, passwd):
        RoadService.registration_inspector(RoadService, log, passwd)


class WhoScreen(Screen):
    pass


class RoadSystemScreen(Screen):
    def registration(self):
        Controller.registration(Controller)

    def authorization(self):
        Controller.registration(Controller)


class DriverActionScreen(Screen):
    pass


class InspectorActionScreen(Screen):
    def view_req(self):
        UserInspector.view_requests(UserInspector)


class RoadInfScreen(Screen):

    def view_feedbacks(self, RoadArea):
        AppUser.view_feedbacks(AppUser, RoadArea)


class RoadInfDrScreen(RoadInfScreen):
    pass


class RoadInfInsScreen(RoadInfScreen):
    def del_road_work(self, RoadWork):
        UserInspector.del_road_work(UserInspector, RoadWork)


class SearchScreen(Screen):
    def view_roads(self):
        AppUser.view_feedbacks(AppUser)


class SearchScreenDr(SearchScreen):
    pass


class SearchScreenIns(SearchScreen):
    pass


class EmptyScreen1(Screen):
    pass


class EmptyScreen2(Screen):
    pass


class ReqAddScreen(Screen):
    def add_road_work(self, area, req):
        UserInspector.add_record_road_work(UserInspector, area, req)


class CommentFormScreen(Screen):
    def add_feedback(self, area, feedback, rate):
        UserDriver.add_feedback(UserDriver, area, feedback, rate)


class DtpFormScreen(Screen):
    def add_ac(self, roadarea):
        UserDriver.add_road_accident(UserDriver, roadarea)


class Comment1Screen(Screen):
    pass


class Comment2Screen(Screen):
    pass


class ReqFormScreen(Screen):
    def add_req(self, roadarea, desc):
        UserDriver.add_request(UserDriver, roadarea, desc)


sm = ScreenManager()

sm.add_widget(RoadSystemScreen(name="rs"))
sm.add_widget(SignUpUScreen(name="signupu"))
sm.add_widget(SignUpIScreen(name="signupi"))
sm.add_widget(SignInScreen(name="signin"))
sm.add_widget(WhoScreen(name="who"))
sm.add_widget(DriverActionScreen(name="dract"))
sm.add_widget(InspectorActionScreen(name="insact"))
sm.add_widget(SearchScreenDr(name="searchdr"))
sm.add_widget(SearchScreenIns(name="searchins"))
sm.add_widget(RoadInfDrScreen(name='rinfdr'))
sm.add_widget(RoadInfInsScreen(name='rinfins'))
sm.add_widget(EmptyScreen1(name="empty1"))
sm.add_widget(EmptyScreen2(name="empty2"))
sm.add_widget(CommentFormScreen(name='comform'))
sm.add_widget(DtpFormScreen(name='addroadac'))
sm.add_widget(ReqFormScreen(name='addreq'))
sm.add_widget(ReqAddScreen(name='reqadd'))
sm.add_widget(Comment1Screen(name='com1'))
sm.add_widget(Comment2Screen(name='com2'))


def set_screen(screen_name):
    sm.current = screen_name


set_screen("rs")


class TransportSystem(App):
    Window.clearcolor = (.73, .72, .76)

    def build(self):
        return sm

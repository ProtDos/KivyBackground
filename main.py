from os.path import join, dirname, realpath

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from plyer import notification
from plyer.utils import platform
from kivy.properties import DictProperty

kivy.require('1.8.0')

a = 0
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass

    SERVICE_NAME = u'{packagename}.Service{servicename}'.format(
        packagename=u'org.test.bg_app',
        servicename=u'Myservice'
    )
    service = autoclass(SERVICE_NAME)
    mActivity = autoclass(u'org.kivy.android.PythonActivity').mActivity
    argument = ''
    service.start(mActivity, argument)


class NotificationDemo(BoxLayout):
    kwargs = DictProperty()

    def update(self, dt):
        global a
        a = a + 1
        message = str(a)
        title = self.ids.notification_title.text
        self.ids.notification_text.text = message
        ticker = self.ids.ticker_text.text
        self.kwargs = {'title': title, 'message': message, 'ticker': ticker}
        print(message)
        notification.notify(**self.kwargs)


class NotificationDemoApp(App):
    def build(self):
        notify = NotificationDemo()
        Clock.schedule_interval(notify.update, 5)
        return notify

    def on_pause(self):
        return True


if __name__ == '__main__':
    NotificationDemoApp().run()

class Commands():
    def cmd_foo(self,arg):
        print("Foo",arg)

    def cmd_f(self,arg):
        print("foo",arg)

    def callFunction(self, name):
       fn = getattr(self, 'cmd_'+name, None)
       if fn is not None:
            fn()

class City:

    def __init__(self, id, latitude, longitude, city, label):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.city = city
        self.label = label

    def id_item(self):
        print(self.id)

foo = "aaa"
bar = "bbb"
call_dict = {
    'foo': foo,
    'bar': bar
}

#call_dict[cmd_bar]("")

cm = Commands()
cm.cmd_foo("bar")
cm.cmd_f("bar")

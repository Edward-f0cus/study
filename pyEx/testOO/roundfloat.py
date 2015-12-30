#!/usr/bin/env python

class RoundFloat(object):
    def __init__(self, val):
        assert isinstance(val, float), "Value must be float"
        self.value = round(val, 2)

    def __str__(self):
        return "%.2f" % self.value

    __repr__ = __str__

#print RoundFloat(5.5655555)
#print RoundFloat(4.2)

class Time60(object):
    def __init__(self, hr, min):
        self.hr = hr
        self.min = min

    def __str__(self):
        return "%s:%s" % (str(self.hr), str(self.min))

    def __add__(self, obj):
        assert isinstance(obj, Time60), "should add with Time60 instance"
        return self.__class__(self.hr + obj.hr, self.min + obj.min)

    def __sub__(self, obj):
        assert isinstance(obj, Time60), "should add with Time60 instance"
        return self.__class__(self.hr - obj.hr, self.min - obj.min)

    def __iadd__(self, obj):
        #return self.__class__(self.hr + obj.hr, self.min + obj.min)
        self.hr += obj.hr
        self.min += obj.min
        return self

rt = RoundFloat(4.555)
t1 = Time60(15, 20)
t2 = Time60(3, 20)
print t1 + t2
print t1 - t2
t1 += t2
print t1
#print t1 + rt


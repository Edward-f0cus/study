#!/usr/bin/env python

import cookielib, urllib2
import urllib

cookiejar = cookielib.CookieJar()
urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
values = {'read_mode': 'day', 'default_font': 'font2', '__utmt': '1',
          'CNZZDATA1253183112': '220655796-1451399390-%7C1451399390',
          '__utma': '194070582.2118541773.1451403617.1451403617.1451403617.1',
          '__utmb': '194070582.2.10.1451403617',
          '__utmc': '194070582',
          '__utmz': '194070582.1451403617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
          '__utmv': '194070582.|2=User%20Type=Visitor=1',
          'remember_user_token': 'W1s3OTg5MzNdLCIkMmEkMTAkRWpiVy5DY0cxbFdrYTlSU3dOVDVFTyJd--fb574f616bd278b54a05fcaa7ad8462491e84c60',
          '_session_id': 'MXBNTUwvblRWMUVuRW1SdmVMOCtHZEVXaXdSZkdNUU4xdVo0QlpVSHBEM2IxdFk4M0pTSlRlVG9mN2ZiTWtLWGxPeXFhSE9wenVmYVJWQlhHN3J3QWNCViswUGx5dVVBaEZVaGFYRHdQUjJpdE1kWjdwVTFpM1lVL2hPaTJaSFdScDkrYzlLYWZUYTBNRFREQmdldkM1dzhKQ3YvS0dGUEoyRTM2YlRTUUxDb2dXT1NMZzZxUEl6K2N2MjBDei9NalVRN2JWKzlXY0g2dXY1d2h4cEVJUzBlbDZCV1ltSFlzZUlWd3lBTHMzVSs3ODJMVk81OUdrancwalA5azgrK3dNV2dxN3ZidjRGQkcvUTJ3NkpHWENsV0c3bHcwdHU1ejRyWDNuU2FYdXloVVgyN2ZQVlRQSnI3QkhNMVZ2Y3BKZ0NhUG1rZitneUR1eC9NU1YvYjBDVUJZQ0dXVEg3bStVVkdadWZ3R2t1aVdyekk3bXFNS2t6N0RFSHB6cXlpNVlZYjBITG0wb2Z2dHd5RDBOclpuYVUvR0FmUTJYVXd5WCtRSHBKd0lyTTlFSzZmSUlENmdDWkVFMnZ6aDZLcTBFYngzWUNwZVNGL3cvWXRXRGZVUEh5bUc2U3pZY2diQzkrMERKUERFRDA9LS12U09MZTkvUVNYbGVTZ05uYUFWdkFBPT0%3D--570b1603e859c1125d65d2e7ac0a2cc89a9116d3'}
data = urllib.urlencode(values)

request = urllib2.Request('http://www.jianshu.com/', data)
url = urlOpener.open(request)
print url.info()
page = url.read()

# request = urllib2.Request(url)
# url = urlOpener.open(request)
# page = url.read()
# print page

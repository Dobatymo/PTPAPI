import os
import os.path
import StringIO
import ConfigParser

confFile = os.path.join(os.environ['HOME'], '.ptpapi.conf')

defaults = {'baseURL': 'https://tls.passthepopcorn.me/',
            'cookiesFile': '~/.ptp.cookies.txt',
            'downloadDirectory': '.'}
default = """
[Main]
baseURL=https://tls.passthepopcorn.me/
cookiesFile=~/.ptp.cookies.txt
downloadDirectory=.

[Reseed]
action=hard
"""
config = ConfigParser.ConfigParser()
config.readfp(StringIO.StringIO(default))
config.read(confFile)

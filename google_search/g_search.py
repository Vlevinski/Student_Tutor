#!/usr/bin/env python3.7
#               @vlevinski
#

try:
    from googlesearch import search
except ImportError:
    print ( " no module named 'google' found")

for url in search('Python learn', stop=5):
    print(url)

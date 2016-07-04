import AddressCleaner
import Environment
address = 'A-12, Connaught Place New Delhi - 110001'
alpha = AddressCleaner.AddressCleaner([',', '+'], address)
alpha.clean_address()
alpha.make_list()
cleanAddress = alpha.get_address()
alpha = Environment.Environment(cleanAddress)
alpha.create()
sample_space = alpha.get_sample_space()

# import urllib
# import json
# import re
# address = address.split(" ")
# address.remove("-")
# sample_space = list()
# for i in itertools.permutations(address):
#     sample_space.append(i)
# print sample_space
# auth_key1 = 'AIzaSyCES_SOJaQQlLBNAI7mSn8jWzQxdklVjIY'
# url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(28.633037) + ',' +
# str(77.217866) + '&radius=500&key=' + auth_key1
# a = urllib.urlopen(url).read()
# b = json.loads(a)
# for c in b['results']:
#     if c['place_id'] == 'ChIJqb5Z2Tf9DDkRO1m9dpuGBLE':
#         print(c['name'])

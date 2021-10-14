# https://en.wikipedia.org/wiki/URL
from pyparsing import *

scheme = Word(alphas, alphanums + "+.-")("scheme")

username = Word(alphanums)("username")
password = Word(alphanums)("password")
userinfo = username + ":" + password

hostname = Word(alphas, alphanums + ".-")("hostname")
ipv4_address = pyparsing_common.ipv4_address("ipv4_address")
ipv6_address = pyparsing_common.ipv6_address("ipv6_address")
host = hostname | ipv4_address | "[" + ipv6_address + "]"

port = Word(nums)("port")

authority = "//" + Optional(userinfo + "@") + host + Optional(":" + port)

segment = Word(alphanums + "%.-_")
path = delimitedList(Optional(segment), "/")("path")

key = Word(alphanums + "%.-_")("key")
value = Word(alphanums + "%.-_")("value")
query = dictOf(key, oneOf("= ;") + value + Optional("&"))("query")

fragment = Word(alphanums)("fragment")

url = scheme + ":" + Optional(authority) + path + Optional("?" + query) + Optional("#" + fragment)

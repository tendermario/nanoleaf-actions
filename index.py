from nanoleaf import Aurora
import requests

ip = '192.168.88.254'
auth_token = 'ZGW3EHNvScT8vpDLDs3T2T8VS6lFeQYC'

my_aurora = Aurora(ip, auth_token)
my_aurora.on = True

url = "http://" + ip + ":16021/api/v1/" + auth_token + "/rhythm/rhythmActive"
r = requests.get(url)
print(r)

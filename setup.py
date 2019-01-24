from nanoleaf import setup

# Uncomment to find the IP address again
ipAddressList = setup.find_auroras(5)

print(ipAddressList)
# Press and hold the power button and then run this to get the token
token = setup.generate_auth_token(ipAddressList[0])

print(token)
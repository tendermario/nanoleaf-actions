# Messing around with Nanoleaf

Setup:

Step 1 (because I'm lazy): turn your python3 into `p`. Open .bashrc or .zshrc and add `alias p='python3'`.

Step 2: alter the nanoleaf setup file located at `/usr/local/lib/python3.7/site-packages/nanoleaf/setup.py` and change line 47 to be `sock.bind(('', 9090))`.

Step 3: figure out your IP and create a token to use by running `p setup.py`. Use that IP and token going forward!

# API

`p on` : turns the unit on
`p off` : turns the unit off
`p random-effect` : changes the effect constantly to something random

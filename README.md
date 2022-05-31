# GitDiscloser
Python recon tool for Github information disclosure research

Install:

$ git clone https://github.com/mathis2001/GitDiscloser

$ cd GitDiscloser

$ python3 gitdiscloser.py

Usage:

./gitdiscloser.py [-h] [-s github search] [-k keyword] [-u]

options:

-h help

-s github search (you can only put target.com or use dorks like "language:python target.com")

-k search for a specific keyword (passwd, password, token, api_token, secret, private, ldap...)

-u search for urls in files (useful to get a larger attack surface)

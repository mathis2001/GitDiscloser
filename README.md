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

Configuration:

In your Github account, clic on your profile in the top right of the page.

Then go to settings > Developer settings > personal access tokens > Generate a new token.

Give a name to your token, select only the public_repo access and clic on "Generate token".

You can now copy your token and paste it in the api.cfg file.

![image](https://user-images.githubusercontent.com/40497633/171192156-1f76f642-2d13-4226-bd4b-63def95aa2b0.png)

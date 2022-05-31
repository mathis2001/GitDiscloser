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

![image](https://user-images.githubusercontent.com/40497633/171192364-aa66b523-cb2f-40e4-bcf2-8b007a1ad682.png)


You can now copy your token and paste it in the api.cfg file.

Some screens:

![image](https://user-images.githubusercontent.com/40497633/171193566-e9b6b4cb-33f2-4833-91db-1487ec5366e5.png)

# GitDiscloser
Python recon tool for Github information disclosure research

## Install:
```bash
$ git clone https://github.com/mathis2001/GitDiscloser

$ cd GitDiscloser

$ python3 gitdiscloser.py
```
## Usage:
```bash
./gitdiscloser.py [-h] [-s "github search"] [-k keyword] [-f wordlist] [-u]
```
## options:
```bash
-h help

-s github search (you can only put target.com or use dorks like "language:python target.com")

-f find possible secrets with a wordlist

-n sort by the more recently indexed (because old secrets can no longer be valid)

-k search for a specific keyword (passwd, password, token, api_token, secret, private, ldap...)

-u search for urls in files (useful to get endpoints and a larger attack surface)
```
## Configuration:

In your Github account, clic on your profile in the top right of the page.

Then go to settings > Developer settings > personal access tokens > Generate a new token.

Give a name to your token, select only the public_repo access and clic on "Generate token".

![image](https://user-images.githubusercontent.com/40497633/171192364-aa66b523-cb2f-40e4-bcf2-8b007a1ad682.png)


You can now copy your token and paste it in the api.cfg file.

## Some screens:

![image](https://user-images.githubusercontent.com/40497633/171377224-106dbd7c-aac7-4684-8fe8-4602470518fb.png)

![test](https://user-images.githubusercontent.com/40497633/171198846-f6cf1d46-87e9-4297-9b10-d47ac858f4a7.png)

![test](https://user-images.githubusercontent.com/40497633/171200623-941d6392-3860-4707-a62b-fc62193787cb.png)

![test](https://user-images.githubusercontent.com/40497633/171198551-7a38fa0a-2ec8-47e5-9641-9737b3706903.png)

![test](https://user-images.githubusercontent.com/40497633/171199524-cb1fec1e-2479-4624-9004-faebb9e835a2.png)

![test](https://user-images.githubusercontent.com/40497633/171377033-91ba2761-18fd-4b75-9158-758d7db21473.png)

## TO DO

- fix bugs
- Add an output file option (you can use "| tee -a" to get an output anyway") 
- Add a limit option

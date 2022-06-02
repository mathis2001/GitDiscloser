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
./gitdiscloser.py [-h] [-s "github search"] [-f wordlist] [-k keyword] [-u] [-n]
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

![image](https://user-images.githubusercontent.com/40497633/171599615-d4ea31ac-a6bb-4d8d-9be7-0ef7a1e6ab33.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171599909-f942bc64-7e95-4c89-8fcd-a190b79dd45b.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171600194-a5504367-0d29-411e-9af2-c05a3fb4899a.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171600770-77d167e8-b95f-4e4b-a234-bc65a4c50cbf.png)
![tempsnip](https://user-images.githubusercontent.com/40497633/171601131-718194d0-2fbf-4eba-8aaf-7623ad8ad950.png)


## TO DO

- fix bugs
- Add an output file option (you can use "| tee -a" to get an output anyway") 
- Add a limit option

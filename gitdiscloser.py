#!/usr/bin/env python3

from github import Github
import sys
from sys import argv
import requests
import re
import os

ACCESS_TOKEN = os.getenv('GITHUB_TOKEN')

token = Github(ACCESS_TOKEN)

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'
	
def banner():
        print('''

   ______   _   _   ______     _                 __
 .' ___  | (_) / |_|_   _ `.  (_)               [  |  by S1rN3tZ
/ .'   \_| __ `| |-' | | `. \ __   .--.   .---.  | |  .--.   .--.  .---.  _ .--.   
| |   ____[  | | |   | |  | |[  | ( (`\] / /'`\] | |/ .'`\ \( (`\]/ /__\\[ `/'`\]  
\ `.___]  || | | |, _| |_.' / | |  `'.'. | \__.  | || \__. | `'.'.| \__., | |      
 `._____.'[___]\__/|______.' [___][\__) )'.___.'[___]'.__.' [\__) )'.__.'[___]     

        ''')

def help():
	print('''
  Options
  --------------------------------------------------------
  	-h   Show this help message
  Search:
	-s   search request
	-u   search for urls in code
	-f   find word matches with a wordlist
	-n   sort by the more recently indexed
	-l   limit (number of results wanted)
	-c   profile information for each result
  Profiling:
  	-r   profile information by repository link
	-p   profile information by username
  Advanced (commits scan):
        -a   repository (mathis/GitDiscloser)
        -f   find word matches in commits with a wordlist
  --------------------------------------------------------
  Config

        Simply put your github token in your environment variables with the name 'GITHUB_TOKEN'.

	''')

def getopts(argv):
	opts = {}  
	while argv:
		try:
			if argv[0][0] == '-':
				opts[argv[0]] = argv[1] 
		except:
			if argv[0] == '-h':
				print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Search: ./gitdiscloser.py [-h] [-s github search] [-f wordlist] [-l limit] [-u] [-n] [-c]")
				print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Profiling: ./gitdiscloser.py [-h] [-r repository link | -p username]")
				print(bcolors.INFO+"[*] "+bcolors.RESET+"Advanced: ./gitdiscloser.py [-h] [-a user/repository] [-f wordlist]")
				help()
				sys.exit(0)
		argv = argv[1:] 
	
	return opts

def gitsearch(input):
	if '-n' in argv:
			query = "sort:indexed "+input
	else:
			query = input
	result = token.search_code(query, order='desc')
	return result

def profiler(source=0):
	myargs = getopts(argv)
	if '-r' in myargs:
		repo = myargs['-r']
		repolist = repo.split("/")
		repolist.pop(1)
		username = repolist[2]
	elif '-p' in myargs:
		username = myargs['-p']
	elif '-c' in argv:
		repo=source
		repolist = repo.split("/")
		repolist.pop(1)
		username = repolist[2]
	
	getuser = token.get_user(username)
	bio = getuser.bio
	email = bcolors.INFO+str(getuser.email)+bcolors.RESET
	firstname = bcolors.INFO+str(getuser.name)+bcolors.RESET
	avatar = getuser.avatar_url
	company = bcolors.INFO+str(getuser.company)+bcolors.RESET
	location = getuser.location
	followers = bcolors.INFO+str(getuser.followers)+bcolors.RESET
	following = bcolors.INFO+str(getuser.following)+bcolors.RESET
	blog = getuser.blog
	creation = getuser.created_at
	update = getuser.updated_at
	output = f'''
	 avatar: {avatar} 
	       ____________________________________________________________________
              [ Profile	                                                      -   x]
              |____________________________________________________________________|
              |						                    
       	      |	username: {username}                        
              |	firstname: {firstname}	                    
              |	bio: {bio}                                  
	      | email: {email}
	      | company : {company}
	      |	location: {location}
              |
	      |	followers: {followers} following: {following}
	      |	
	      |	website: {blog}
              [____________________________________________________________________
         created at: {creation}
	last update: {update}
	'''
	print(output)

def search_urls(source):
	r = requests.get(source)
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	match = re.findall(regex,r.text)
	return match

def search_secrets(source):
	myargs=getopts(argv)
	if '-f' in myargs:
		wordlist = myargs['-f']
		SecretList=[]
		FinalList=[]
		r = requests.get(source)
		print(bcolors.INFO+"\n Possible secret(s) found in file:\n"+bcolors.RESET)
		with open(wordlist) as l:
			for word in l:
				word = word.splitlines()
				word = ' '.join(word)
				SecretMatch = re.findall(word,r.text)
				for find in SecretMatch:
					SecretList.append(find)
					for secret in SecretList:
						if secret not in FinalList:
							FinalList.append(secret)
		for SecretFind in FinalList:
			print(bcolors.OK+" [+] "+bcolors.RESET+SecretFind+"\n")
	else:
		pass

def commit_scan(reposit):
	myargs = getopts(argv)
	repo = token.get_repo(reposit)

	commits = repo.get_commits()
	
	if '-l' in myargs:
		limit=int(myargs['-l'])

	for commit in commits[:limit]:
		commit_url = commit.commit.html_url
		print(bcolors.OK+"[+] "+bcolors.RESET+commit_url)
		search_secrets(commit_url)

def main():
	myargs = getopts(argv)
	if len(argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Search: ./gitdiscloser.py [-h] [-s github search] [-f wordlist] [-l limit] [-u] [-n] [-c]")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: Profiling: ./gitdiscloser.py [-h] [-r repository link | -p username]")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Advanced: ./gitdiscloser.py [-h] [-a user/repository] [-f wordlist]")
		sys.exit(0)
	rate_limit = token.get_rate_limit()
	rate = rate_limit.search
	if rate.remaining == 0:
		print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}.')
	else:
		print(f'You have {rate.remaining}/{rate.limit} API calls remaining.')
	if '-a' in myargs:
		commit_scan(myargs['-a'])
	
	if not '-s' in myargs:
		if not '-a' in myargs:
			profiler()
			print('test')
		
	if '-s' in myargs:
		result=gitsearch(myargs['-s'])
		max_size = 100
		print(f'Found {result.totalCount} file(s):')
		
		if '-l' in myargs:
			limit = int(myargs['-l'])
			result = result[:limit]

		elif result.totalCount > max_size:
			result = result[:max_size]

		for file in result:
			url=f'{file.download_url}'
			print(bcolors.OK+"[+] "+bcolors.RESET+url)
			if '-c' in argv:
				profiler(url)
			else:
				pass

			if '-u' in argv:
				match=search_urls(url)
				print(bcolors.INFO+"\n URL(s) found in file:\n"+bcolors.RESET)
				for Url in match:
					print(bcolors.INFO+"[*] "+bcolors.RESET+Url[0])
			else:
				pass

			search_secrets(url)
				

if __name__ == '__main__':
	try:
		banner()
		main()
	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
        	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")


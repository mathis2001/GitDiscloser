from github import Github
import sys
from sys import argv
import requests
import re
import configparser

config = configparser.RawConfigParser()
config.read('api.cfg')
ACCESS_TOKEN = config.get('Github', 'token')

token = Github(ACCESS_TOKEN)

class bcolors:
	OK = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	RESET = '\033[0m'
	INFO = '\033[94m'

def help():
	print('''
  Options
  -------------------------------------------
	-h   help
	-t   target
	-o   output file
	-u   search for urls in code
	-k   search for keyword
  -------------------------------------------
	''')

def getopts(argv):
	opts = {}  
	while argv:
		try:
			if argv[0][0] == '-':
				opts[argv[0]] = argv[1] 
		except:
			if argv[0] == '-h':
				print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./main.py [-h] -t target.com [-u] [-k] [-o output file]")
				help()
				sys.exit(0)
		argv = argv[1:] 
	return opts

def main():
	myargs = getopts(argv)
	if len(sys.argv) < 2:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"No target given.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"usage: ./cert4recon.py [-h] -t target.com [-o output file] [-a]")
		sys.exit(0)
	rate_limit = token.get_rate_limit()
	rate = rate_limit.search
	if rate.remaining == 0:
		print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}.')
	else:
		print(f'You have {rate.remaining}/{rate.limit} API calls remaining.')
	
	if '-t' in myargs:
		query = myargs['-t']
	result = token.search_code(query, order='desc')

	max_size = 100
	print(f'Found {result.totalCount} file(s):')
	if result.totalCount > max_size:
		result = result[:max_size]

	for file in result:
		url=f'{file.download_url}'
		print(bcolors.OK+"[+] "+bcolors.RESET+url)
		if '-u' in sys.argv:
			r = requests.get(url)
			regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
			match = re.findall(regex,r.text)
			print("\n URL(s) found in file:\n")
			for Url in match:
				print(bcolors.INFO+"[*] "+bcolors.RESET+Url[0])

		if '-k' in myargs:
			r = requests.get(url)
			reg = myargs['-k']
			count=0
			keyMatch = re.findall(reg,r.text)
			if reg in keyMatch:
				print(bcolors.OK+"[+] "+bcolors.RESET+"Keyword found !")
			for keyword in keyMatch:
				count = count+1
			print(bcolors.INFO+"[*] "+bcolors.RESET+"Keyword matched "+str(count)+" time(s). \n")

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(bcolors.FAIL+"[!] "+bcolors.RESET+"A problem has occured.")
		print(bcolors.INFO+"[*] "+bcolors.RESET+"Error info:")
		print(e)
	except KeyboardInterrupt:
        	print(bcolors.FAIL+"[!] "+bcolors.RESET+"Script canceled.")

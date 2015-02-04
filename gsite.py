'''
Quick script for uploading to the google site quickly and easily

usage:
	python /path/to/repo/gsite.py image_name
'''

import os, sys

# file you want to host
fname = sys.argv[1]

# i store mine in a folder figs in the repository
dir = "~/images/."
print dir

# copy the file to the git repo
os.system("cp %s %s" % (fname, dir))

# commit the file to the repo and push to github
os.system("cd %s; git checkout gh-pages; git add %s; git commit -am 'Added %s'; git push origin gh-pages;" % (dir, fname, fname) )

# here's my url
url = "http://smangham.github.io/images/%s" % fname

# copy it to clipboard
os.system("echo '%s' | pbcopy" % url)






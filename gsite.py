'''
Quick script for uploading to the google site quickly and easily

usage:
	python /path/to/repo/gsite.py image_name
'''

import os, os.path, sys

# file you want to host
fname = sys.argv[1]

# i store mine in a folder figs in the repository
dir = "~/images/."
print dir

# copy the file to the git repo
os.system("cp %s %s" % (fname, dir))

# if the file is an eps, convert it to png
fbase = os.path.splitext(fname)[0]
fext  = os.path.splitext(fname)[1]

if fext in ['.eps','.ps','.svg']: 
	os.system("cd %s; convert -density 300 %s -size 1024x840 %s.png" % (dir, fname, fbase))
	fname="%s.png" % fbase

# commit the file to the repo and push to github
os.system("cd %s; git checkout gh-pages; git add %s; git commit -am 'Added %s'; git push origin gh-pages;" % (dir, fname, fname) )

# here's my url
url = "http://smangham.github.io/images/%s" % fname

# copy it to clipboard
os.system("echo '%s' | pbcopy" % url)






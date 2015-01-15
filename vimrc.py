import sys, os, shutil

if len(sys.argv) > 1:
  dir = sys.argv[1]
else:
  dir = raw_input("input dest dir: ")

os.system("git clone --recursive https://github.com/asek-ll/vimrc.git %s" % dir)

vimrcfile = "%s/vimrc" % dir

with open(vimrcfile, 'w') as outfile:
    with open("%s/vimrc.default" % dir, 'r') as infile:
        rowIter = iter(infile)
        for row in rowIter:
            if row.startswith("let $VIMBASE"):
                outfile.write( "let $VIMBASE = '%s' \n" % os.path.dirname(os.path.abspath(vimrcfile)))
            else:
                outfile.write(row)

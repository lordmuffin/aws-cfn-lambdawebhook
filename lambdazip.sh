#!/bin/bash
(echo "### Running Git Clone"; git clone $CIRCLE_REPOSITORY_URL $HOME/$CIRCLE_PROJECT_REPONAME)
(echo "### Make Zip Folder"; sudo mkdir $HOME/upload; )
(echo "### Zipping Lambda Files";cd $HOME/$CIRCLE_PROJECT_REPONAME/functions/; sudo zip -r9 $zipfile *)
(echo "### Zipping Site-Packages"; cd $VIRTUAL_ENV/lib/python2.7/site-packages; sudo zip -r9 $zipfile *)
echo "### Good or bad im done. $zipfile Created."

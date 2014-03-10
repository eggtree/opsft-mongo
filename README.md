opsft-mongo
===========

#local test
tox
# local server, port 5002
tox -e web




mkdir example
cd exmple
# create a python-2.7 application on openshift, call opsmng
# it will clone code from github into another git repo on the openshift node
rhc app create -a opsmng -t python-2.7 --from-code=https://github.com/eggtree/opsft-mongo.git
rhc cartridge add mongodb-2.4 -a opsmng

# push data to the openshift instance, 
# where <ssh-login> is the SSH entry from executing 'rhc app show opsmng'
rsync -avz test.json <ssh-login>:~/app-root/data

rhc app restart opsmng

# hitting the root url of the app should show a count of the number of documents in the issuer collection

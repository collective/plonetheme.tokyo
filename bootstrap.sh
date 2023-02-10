#/bin/sh
`which python3` -m venv venv
./venv/bin/pip install -r requirements.txt
./venv/bin/buildout bootstrap
./bin/buildout -c develop.cfg

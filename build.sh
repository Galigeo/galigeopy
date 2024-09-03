# Remove the old build and dist folders
rm -rf build dist galigeopy.egg-info

# Build
./env/bin/python3 -m pip install --upgrade pip
./env/bin/pip install setuptools wheel
./env/bin/python3 setup.py sdist bdist_wheel
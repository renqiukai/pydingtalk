rm -rf build
rm -rf dist
rm -rf pydingtalk.egg-info

python setup.py sdist build
twine upload dist/*

rm -rf build
rm -rf dist
rm -rf pydingtalk.egg-info
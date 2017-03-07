import pip #needed to use the pip functions

expected = ["virtualenv", "six", "setuptools", "python-mimeparse", "python-dateutil", "psycopg2", "pip", "lxml", "Django", "django-tastypie", "defusedxml", "gnureadline"]
versions = {"virtualenv" : "15.1.0", "six" : "1.10.0", "setuptools" : "28.8.0", "python-mimeparse" : "1.6.0", "python-dateutil" : "2.6.0", "psycopg2" : "2.7", "pip" : "9.0.1", "lxml" : "3.7.3", "Django" : "1.10.5", "django-tastypie" : "0.13.3", "defusedxml" : "0.5.0", "gnureadline" : "6.3.3"}

actual_raw = []
for i in pip.get_installed_distributions(local_only=True):
    actual_raw.append(i)

actual_packages = []
actual_versions = {}
for i in actual_raw:
	pkg, ver = str(i).split(' ')
	actual_packages.append(pkg)
	actual_versions[pkg] = ver

for i in actual_packages:
	if i not in expected:
		print("Found unexpected package " + i)
	elif actual_versions[i] != versions[i]:
		print("Found expected package " + i + " but found version " + actual_versions[i] + " when version " + versions[i] + "was expected.")

for i in expected:
	if i not in actual_packages:
		print("Did not find expected package " + i + ". Please install " + i + " version " + versions[i] + ".")



import imp
import os
import sys

# This is a namecheap-specific launch file that changes their default template
# to use the structure of this project

# To reuse, ensure a module named "src" with a file named "app.py"
# containing the flask application is available
sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'src/app.py')
application = wsgi.app

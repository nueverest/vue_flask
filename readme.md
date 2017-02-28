# vue_flask
Responsive AWS Serverless SPA using Vue.js, Flask, Firebase, and more.

# Benefits of Serverless
Serverless operations do use a server, but it only runs 20-60 milliseconds at a time.
- High Performance
- High Availability
- High Scalability
- No Server and associated infrastructure to understand and maintain.
- Easy undeployment

# Disadvantage of Serverless
- Deployment and Update actions require the entire project to be uploaded. Even a tiny change such as adding one 
semi-colon to a file requires the full project to be uploaded.  Projects take minutes to upload.

# Technologies Used
- Vue.js - Frontend Javascript Framework https://vuejs.org/
- Vuefire - Firebase Anonymous Authentication https://github.com/chrisbraddock/vuefire-auth-demo
- Flask - Python Web Framework http://flask.pocoo.org/
- Flask-S3 - Serve Static Media from AWS S3. https://flask-s3.readthedocs.io/en/latest/
- Firebase - Realtime Persistent Datastore https://firebase.google.com/
- Zurb Foundation 6 - CSS Frontend Framework http://foundation.zurb.com/
- Blowdrycss - Python Atomic CSS compiler https://github.com/nueverest/blowdrycss
- Google Material Icons - Icons that behave like fonts https://google.github.io/material-design-icons/
- Zappa - Python serverless deployment interface https://github.com/Miserlou/Zappa
- Amazon Web Services (AWS) - Cloud Infrastructure - S3, Lambda, API Gateway, CloudWatch, IAM https://aws.amazon.com/

# Requirements
- Python 2.7.x (Zappa will NOT work with Python 3.x because AWS Lambda is only 2.7.x compatible.)
- See requirements.txt

# How to Setup Firebase
- Setup a firebase account.
- In firebase, click "Create New Project".
- Open the project.
- On the Overview page for your project click "Add Firebase to your web app".
- Use this data to replace apiKey, authDomain, databaseURL, storageBucket, and messagingSenderId in `templates/index.html`.

# Change Flask-S3 Config in vue_flask.py
- app.config['FLASKS3_BUCKET_NAME'] = 'your_s3_bucket_name_here'

# Setup Sass and SCSS Transpiler
- Download and Install Ruby http://www.ruby-lang.org/en/downloads/
- Setup system path for Ruby
- At command prompt enter `gem install sass` to install sass.
- If you are using an IDE like PyCharm you can setup a File Watcher https://www.jetbrains.com/help/pycharm/2016.3/transpiling-sass-less-and-scss-to-css.html#intro
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439

# Combine Javascript files into one and minify with uglifyjs 
- Open command line as Administrator.
- Run `npm install -g concat-cli` the `-g` installs concat-cli globally.
- Run `npm list -g --depth=0` to confirm installation.
- To manually run use `concat-cli -f jquery.js what-input.js foundation.js -o combined.js` reference: https://www.npmjs.com/package/concat-cli
- Setup a custom File Watcher for PyCharm.

# Setup auto-minify CSS and JS using node.js yuicompress
- Install node package manager (npm) on your machine.
- Place npm on the system path.
- Open command line as Administrator.
- Run `npm install -g yuicompressor` the `-g` installs the yuicompressor globally.
- Run `npm list -g --depth=0` to confirm installation.
- Setup a File Watcher for YUI CSS and YUI JS https://www.jetbrains.com/help/pycharm/2016.3/minifying-css.html
- Configuring File Watcher output path http://stackoverflow.com/a/36038914/1783439

# How to Deploy using Zappa - Serverless.
- Create and Activate a virtual environment for this project. Reference: https://virtualenv.pypa.io/en/stable/installation/
- `pip install requirements.txt`
- Place aws credentials with correct permissions in `<path to user folder>\.aws\credentials` Reference: https://github.com/Miserlou/Zappa/issues/244
- Open zappa_settings.json and change "s3_bucket" and "aws_region" to match your AWS account.
- `zappa deploy production`
- Navigate to generated url.

# How to Update Deployment
- `zappa update production`

# How to Undeploy
- `zappa undeploy production`

# Helpful notes about deployment.
- Combine, minify, and gzip CSS files.
- Combine, minify, and gzip JS files.
- You can use `gzip -9 filename.css`. The `-9` provides the best compression.
- Zopfli https://github.com/obp/zopfli developed by Google is more powerful and may one day be integrated with this project.
- Upload these two files to S3 and make the files public http://www.rightbrainnetworks.com/blog/serving-compressed-gzipped-static-files-from-amazon-s3-or-cloudfront/
- AWS Cloudfront is a CDN that can be linked to your S3 bucket. A Content Delivery Network (CDN) places the data closer to the end user by storing your files all over the world.
- Enable file Caching so that browsers do not need to download the files every time the page loads.

# Testing with Flask-Testing, Selenium, Google chromedriver, Mozilla geckodriver
- Google chromedriver https://sites.google.com/a/chromium.org/chromedriver/downloads
- Mozilla geckodriver https://github.com/mozilla/geckodriver/releases
- Microsoft edge webdriver https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- Microsoft Internet Explorer http://selenium-release.storage.googleapis.com/index.html
- Mac Safari webdriver https://webkit.org/blog/6900/webdriver-support-in-safari-10/
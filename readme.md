# vue_flask
Responsive AWS Serverless SPA using Vue.js, Flask, Firebase, and more.

# Live Serverless Demo
https://kw4udfbos9.execute-api.us-west-2.amazonaws.com/production

# Benefits of Serverless
Serverless operations do use a server, but it only runs 20-60 milliseconds at a time.
- High Performance
- High Availability
- High Scalability
- No Server and associated infrastructure to understand and maintain.
- Easy undeployment

# Disadvantage of Serverless
- Deployment and Update actions require the entire project to be uploaded. Even a tiny change such as adding one 
character to a file requires the full project to be uploaded.  Projects take minutes to upload.

# Technologies Used
- Vue.js - Frontend Javascript Framework https://vuejs.org/
- Vuefire - Firebase Anonymous Authentication https://github.com/chrisbraddock/vuefire-auth-demo
- Flask - Python Web Framework http://flask.pocoo.org/
- Flask-S3 - Serve Static Media from AWS S3. https://flask-s3.readthedocs.io/en/latest/
- Firebase - Realtime Persistent Datastore https://firebase.google.com/
- Zurb Foundation 6 - CSS Frontend Framework http://foundation.zurb.com/
- Blowdrycss - Python Atomic CSS compiler https://github.com/nueverest/blowdrycss
- Google Material Icons - Icons that behave like fonts https://google.github.io/material-design-icons/
- SCSS - Sassy CSS a superset of CSS3's syntax.
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

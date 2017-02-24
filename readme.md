# vue_flask
Serverless implementation of Vue.js, Flask, and Firebase

# Features
- Vue.js Javascript Frontend
- Zurb Foundation 6 CSS Frontend Framework
- Flask Python Backend
- Realtime Firebase Data Management

# Requirements
- Python 2.7.x
- See Requirements.txt

# How to Setup Firebase
- Setup a firebase account.
- In firebase, click "Create New Project".
- Open the project.
- On the Overview page for your project click "Add Firebase to your web app".
- Use this data to replace apiKey, authDomain, databaseURL, storageBucket, and messagingSenderId in `templates/index.html`.

# How to Deploy
- Create and Activate a virtual environment for this project. Reference: https://virtualenv.pypa.io/en/stable/installation/
- `pip install zappa`
- Place aws creditials with correct permissions in <path to user folder>\.aws
- Open zappa_settings.json and change "s3_bucket" and "aws_region" to match your AWS account.
- `zappa deploy dev`
- Navigate to generated url.

# How to Update Deployment
- `zappa update dev`

# How to Undeploy
- `zappa undeploy dev`
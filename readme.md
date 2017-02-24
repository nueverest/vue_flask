# vue_flask
Serverless implementation of Vue.js, Flask, and Firebase

# Technologies Used
- Vue.js - Frontend Javascript Framework https://vuejs.org/
- Vuefire - Firebase Anonymous Authentication https://github.com/chrisbraddock/vuefire-auth-demo
- Flask - Python-Based Web Framework http://flask.pocoo.org/
- Flask-S3 - Serve Static Media from AWS S3. https://flask-s3.readthedocs.io/en/latest/
- Firebase - Realtime Persistent Datastore https://firebase.google.com/
- Zurb Foundation 6 - CSS Frontend Framework http://foundation.zurb.com/
- Blowdrycss - Python-based Atomic CSS compiler https://github.com/nueverest/blowdrycss
- Zappa - Python-based serverless deployment interface https://github.com/Miserlou/Zappa
- Amazon Web Services (AWS) - Cloud Infrastructure https://aws.amazon.com/

# Requirements
- Python 2.7.x (Zappa will NOT work with Python 3.x because AWS Lambda is only 2.7.x compatible.)
- See requirements.txt

# How to Setup Firebase
- Setup a firebase account.
- In firebase, click "Create New Project".
- Open the project.
- On the Overview page for your project click "Add Firebase to your web app".
- Use this data to replace apiKey, authDomain, databaseURL, storageBucket, and messagingSenderId in `templates/index.html`.

# How to Deploy using Zappa - Serverless.
- Create and Activate a virtual environment for this project. Reference: https://virtualenv.pypa.io/en/stable/installation/
- `pip install requirements.txt`
- Place aws credentials with correct permissions in `<path to user folder>\.aws\credentials` Reference: https://github.com/Miserlou/Zappa/issues/244
- Open zappa_settings.json and change "s3_bucket" and "aws_region" to match your AWS account.
- `zappa deploy dev`
- Navigate to generated url.

# How to Update Deployment
- `zappa update dev`

# How to Undeploy
- `zappa undeploy dev`

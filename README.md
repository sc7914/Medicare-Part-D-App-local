# Medicare-Part-D-App-local
Setup
Create virtual environment:

conda create -n ump-env python=3.11
Activate the environment:

conda activate ump-env
Install packages:

#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt
Usage
Medicare Part D spending:

python -m app.medicare
Pull revenue:

python -m app.revenue
Pull calculate exposure:

python -m app.exposure

# Run the web app (then view in the browser at http://localhost:5000/):

# Mac OS:
FLASK_APP=web_app flask run

export FLASK_APP=web_app
flask run

##Testing

# Medicare-Part-D-App-local
#Setup
#Create virtual environment:

conda create -n ump-env python=3.12

#Activate the environment:

conda activate ump-env

#Install packages:

#pip install requests
#pip install plotly
#pip install python-dotenv

# best practice to list the packages in the requirements.txt file:
pip install -r requirements.txt

#Usage:

#Medicare Part D spending:
python -m app.medicare

#Pull revenue:
python -m app.revenue

#Calculate exposure:
python -m app.exposure

def fetch_stocks_csv():
	# Function implementation
	pass

def company_data():
	# Function implementation
	pass

def format_usd(value):
	# Function implementation
	return f"${value:,.2f}"

# Run the web app (then view in the browser at http://localhost:5000/):

# Mac OS:
export FLASK_APP=web-app/app.py
FLASK_APP=web_app/app.py flask run

flask run

##Testing

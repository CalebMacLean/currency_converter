# Imports
from flask import Flask, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests

# App Configurations
app = Flask(__name__)

app.config['SECRET_KEY'] = '1ts2Secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']  = False
app.debug = True

toolbar = DebugToolbarExtension(app)

# Session Key and API Variables 


# Application
@app.route('/', endpoint='home')
def view_home():
    """Renders home page template"""
    return render_template("home.html")

@app.route('/convert', methods=["GET"])
def get_converted_answer():
    """Interacts with the API to convert an amount from one currency to another"""
    
    og_currency = request.args.get('from-input').upper()
    new_currency = request.args.get('to-input').upper()
    amount = str(request.args.get('amount-input'))
    api_url = f"https://api.exchangerate.host/convert?from={og_currency}&to={new_currency}&amount={amount}"

    symbols_response = requests.get('https://api.exchangerate.host/symbols')
    symbols_data = symbols_response.json()
    response = requests.get(api_url)

    # Raise error if invalid currency code is passed
    if(not (og_currency in symbols_data['symbols'])):
        flash( f"Not a valid code: {og_currency}", category='error')
        return redirect('/')
    
    # Raise error if invalid currency code is passed
    if(not (new_currency in symbols_data['symbols'])):
        flash( f"Not a valid code: {og_currency}", category='error')
        return redirect('/')
    
    # Raise error if invalid currency code is passed
    if(not (amount.isnumeric())):
        flash("Not a valid amount", category='error')
        return redirect('/')
    
    # Flash conversion result
    if(response.status_code == 200):
        api_data = response.json()
        flash(f"The result is {round(api_data['result'], 2)} {symbols_data['symbols'][new_currency]['description']}", category="message")
        
        return redirect('/')

    # Raise vague error in case of API request failure
    else:
        flash("Error in currency conversion API request.", category="error")
        return redirect('/')
    
@app.route('/currency-codes', endpoint='currency-codes')
def view_curr_codes():
    """Page that list out valid currency codes to convert"""

    symbols_response = requests.get('https://api.exchangerate.host/symbols')
    symbols_data = symbols_response.json()

    return render_template('codes.html', curr_codes = symbols_data['symbols'],
                           descriptions = [symbols_data['symbols'][code]['description'] for code in symbols_data['symbols']])




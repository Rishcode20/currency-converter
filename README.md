# Currency Converter

A Python + Streamlit app that converts between currencies using live exchange rate data from a public REST API, with a 30-day historical rate chart.

**Live app:** https://currency-converter-airt2dabfnjgl4qtn5dro8.streamlit.app/

## Features
- Convert between any two supported currencies using live exchange rates
- View a 30-day historical rate chart for the selected currency pair
- Handles invalid input and failed API requests gracefully with clear error messages

## Built With
- Python
- [Streamlit](https://streamlit.io/) — UI framework
- [Frankfurter API](https://www.frankfurter.app/) — free exchange rate data, no API key required
- Pandas — data handling for the historical chart

## Running Locally
```bash
git clone https://github.com/Rishcode20/currency-converter.git
cd currency-converter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## What I Learned
Built this to get hands-on practice with REST APIs, Git branching/PR workflows, and deploying a Python app end-to-end.

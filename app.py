import streamlit as st
from converter import convert
import requests
import pandas as pd

st.title("Currency Converter")
st.caption("Live exchange rates powered by the Frankfurter API")

amount = st.number_input("Amount", min_value=0.0, value=100.0)
from_currency = st.text_input("From currency", "USD")
to_currency = st.text_input("To currency", "CAD")

if st.button("Convert"):
    try:
        result = convert(amount, from_currency, to_currency)
        st.write(f"{amount} {from_currency} = {result:.2f} {to_currency}")
    except ValueError as e:
        st.error(str(e))

st.subheader("Last 30 Days")

history_url = f"https://api.frankfurter.app/{pd.Timestamp.today() - pd.Timedelta(days=30):%Y-%m-%d}..?from={from_currency}&to={to_currency}"
history_response = requests.get(history_url)

if history_response.status_code == 200:
    history_data = history_response.json()
    rates = history_data['rates']
    df = pd.DataFrame([(date, values[to_currency]) for date, values in rates.items()], columns=['Date', 'Rate'])
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    st.line_chart(df.set_index('Date'))
else:
    st.write("Couldn't load historical data.")
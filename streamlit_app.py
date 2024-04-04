import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

st.title("Stock Price Tracker")

ticker_symbol = st.text_input(
    "Enter the ticker symbol (e.g., GOOGL, AAPL, MSFT)", value="GOOGL"
)

data = yf.Ticker(ticker_symbol)

# get historical market data
hist = data.history(period="5d")

fig = go.Figure(
    data=[
        go.Candlestick(
            x=hist.index,
            open=hist["Open"],
            high=hist["High"],
            low=hist["Low"],
            close=hist["Close"],
        )
    ]
)

fig.update_layout(
    title="Stock Price Data", yaxis_title="Stock Price (USD)", xaxis_title="Date"
)

st.plotly_chart(fig)

st.write("Current stock price: ", hist["Close"][-1])

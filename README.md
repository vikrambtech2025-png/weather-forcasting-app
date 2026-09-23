# Weather Forecasting App

A lightweight **Flask weather API** that returns current weather for any city using the [OpenWeatherMap](https://openweathermap.org/) API.

## Endpoint

```
GET /weather?city=<city-name>
```

Example:

```bash
curl "http://127.0.0.1:5000/weather?city=Chennai"
```

Returns the raw OpenWeatherMap JSON (temperature in Celsius).

## Setup

```bash
pip install -r requirements.txt
python app.py
```

> **Note:** the app reads the API key from an environment variable. Set your key before running and make sure the variable name referenced in `app.py` matches — keep keys out of committed code.

## License

No license specified — for learning/reference use.
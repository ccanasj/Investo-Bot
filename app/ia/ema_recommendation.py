import yfinance as yf


def getStock(symbol: str, start_date: str):
    return yf.download(symbol, start=start_date, progress=False)

def getInfo(symbol: str):
    ticker = yf.Ticker(symbol).info
    ticker.pop("companyOfficers")
    return ticker

def calculateEMA(data: dict):
    # Calcular las medias móviles exponenciales
    ema_short = data['Close'].ewm(span=20, adjust=False).mean()
    ema_long = data['Close'].ewm(span=50, adjust=False).mean()

    # Crear una nueva columna en el DataFrame con las diferencias entre las medias móviles
    data['ema_diff'] = ema_short - ema_long
    return [ema_short, ema_long, data]


def determineActions(data: dict, symbol: str):
    # Determinar si la acción debería ser comprada, vendida o mantenida
    last_ema_diff = data['ema_diff'][-1]

    if last_ema_diff > 0:
       return f"Se recomienda que la acción de {symbol} debería ser comprada"
    elif last_ema_diff < 0:
       return f"Se recomienda que la acción de {symbol} debería ser vendida"
    else:
       return f"Se recomienda que laa acción de {symbol} debería ser mantenida"
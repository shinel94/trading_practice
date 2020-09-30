from pdreader.pdreader import PDReader
from datetime import datetime

pdreader = PDReader()

start_date = datetime(2020, 9, 1)
end_date = datetime(2020, 9, 30)
yp = pdreader.search_by_code('000670.KS')
yp['MA5'] = yp['Close'].rolling(window=5).mean()
yp['MA20'] = yp['Close'].rolling(window=20).mean()
yp['MA60'] = yp['Close'].rolling(window=60).mean()
yp['MA120'] = yp['Close'].rolling(window=120).mean()
print(yp)
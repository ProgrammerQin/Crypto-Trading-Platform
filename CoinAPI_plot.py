#   This python file is to test and demonstrate coinAPI using Plot function

#   Alpha vantage API key free:  AEGJDU540F597MXQ

#   git clone https://github.com/RomelTorres/alpha_vantage.git
#   pip install -e alpha_vantage
#   python -m pip install SomePackage
#   pip3 install alpha_vantage
#   pip3 install gitpython

from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt

ts = TimeSeries(key='AEGJDU540F597MXQ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='MSFT',interval='10min', outputsize='full')
data['4. close'].plot()
plt.title('Intraday Times Series for the MSFT stock (1 min)')
plt.show()

from statsmodels.tsa.stattools import adfuller

def test_stationarity(x):
    """test the stationarity of a time series using the augmented Dickey Fuller test.
    See the documentation for the object returned."""
    results = adfuller(x)
    print(f"Test statistic: {results[0]:.3f}")
    print(f"p-value: {results[1]:.3f}")
    print(f"Number of lags used: {results[2]}")
    print(f"Critical value, 1 %: {results[4]['1%']:.3f}")
    print(f"Critical value, 5 %: {results[4]['5%']:.3f}")
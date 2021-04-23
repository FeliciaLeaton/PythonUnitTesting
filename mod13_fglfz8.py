import unittest
from project3 import timeSeriesValidation, symbolValidation, chartValidation, startDateValidation, endDateValidation
# You should write unit tests for the five inputs from the stock visualizer challenge that enforce the following constraints.
# symbol: capitalized, 1-7 alpha characters
# chart type: 1 numeric character, 1 or 2
# time series: 1 numeric character, 1 - 4
# start date: date type YYYY-MM-DD
# end date: date type YYYY-MM-DD

class TestStockVisualizer(unittest.TestCase):

    def test_symbol(self):
        self.assertEqual(symbolValidation('GOOGL'),True)
        self.assertEqual(symbolValidation('Googl'),False)
        self.assertEqual(symbolValidation('HELLOOOO'),False)

    def test_charttype(self):
        self.assertEqual(chartValidation('1'),True)
        self.assertEqual(chartValidation('2'),True)
        self.assertEqual(chartValidation('3'),False)
        self.assertEqual(chartValidation('4'),False)
        self.assertEqual(chartValidation('a'),False)
     
    def test_timeseries(self):
        self.assertEqual(timeSeriesValidation('1'),True)
        self.assertEqual(timeSeriesValidation('2'),True)
        self.assertEqual(timeSeriesValidation('3'),True)
        self.assertEqual(timeSeriesValidation('4'),True)
        self.assertEqual(timeSeriesValidation('5'),False)
        self.assertEqual(timeSeriesValidation('a'),False)

    def test_startdate(self):
        self.assertEqual(startDateValidation('201231'),False)
        self.assertEqual(startDateValidation('02-02-2013'),False)
        self.assertEqual(startDateValidation('2013-02-02'),True)
        self.assertEqual(startDateValidation('2014-11-16'),True)

    def test_enddate(self):
        self.assertEqual(endDateValidation('201231'),False)
        self.assertEqual(endDateValidation('02-02-2013'),False)
        self.assertEqual(endDateValidation('2013-02-02'),True)
        self.assertEqual(endDateValidation('2014-11-16'),True)

if __name__ == '__main__':
    unittest.main()

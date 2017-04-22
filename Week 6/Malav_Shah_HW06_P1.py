import unittest
import datetime
from unittest import TestCase

def main():

    target1 = datetime.date(2000, 1, 1)
    target2 = datetime.date(2016, 10, 3)

    # dates is a list of dates
    dates = [
        datetime.date(2010, 1, 15),
        datetime.date(2012, 6, 29)
    ]

     # loop through each of the dates and compare to the target1 and target2
    for date in dates:
        # print number of days between date and target1
        if target1 > date:
            print('There are', computeDays(target1, date), 'days between', target1, 'and', date)
            print('There are', computeMonths(target1, date), 'months between', target1, 'and', date)
            print('There are', computeYears(target1, date), 'years between', target1, 'and', date)

        else:
            print('There are', computeDays(date, target1), 'days between', date, 'and', target1)
            print('There are', computeMonths(date, target1), 'months between', date, 'and', target1)
            print('There are', computeYears(date, target1), 'years between', date, 'and', target1)

        # print number of days between date and target11
        if target2 > date:
            print('There are', computeDays(target2, date), 'days between', target2, 'and', date)
            print('There are', computeMonths(target2, date), 'months between', target2, 'and', date)
            print('There are', computeYears(target2, date), 'years between', target2, 'and', date)

        else:
            print('There are', computeDays(date, target2), 'days between', date, 'and', target2)
            print('There are', computeMonths(date, target2), 'months between', date, 'and', target2)
            print('There are', computeYears(date, target2), 'years between', date, 'and', target2)


def computeDays(date1, date2):
    if date1 > date2:
        return (date1 - date2).days
    else:
        return (date2 - date1).days

def computeMonths(date1, date2):
    if date1 > date2:
        return int((date1 - date2).days / 30.4)
    else:
        return int((date2 - date1).days / 30.4)

def computeYears(date1, date2):
    if date1 > date2:
        return int((date1 - date2).days / 365.25)
    else:
        return int((date2 - date1).days / 365.25)


class TestComputeDays(TestCase):

    def test_computeDays(self):
        dt1 = datetime.date(2000, 1, 1)
        dt2 = datetime.date(2016, 10, 3)
        self.assertEqual(computeDays(dt1, dt2), 6120)

    def test_computeMonths(self):
        dt1 = datetime.date(2000, 1, 1)
        dt2 = datetime.date(2016, 10, 3)
        self.assertEqual(computeMonths(dt1, dt2), 201)

    def test_computeYears(self):
        dt1 = datetime.date(2000, 1, 1)
        dt2 = datetime.date(2016, 10, 3)
        self.assertEqual(computeYears(dt1, dt2), 16)

if __name__ == '__main__':
    unittest.main(exit=False)
    main()

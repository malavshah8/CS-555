import unittest
import datetime
from unittest import TestCase

def main():
    """ Write and test code to demonstrate calculating the number of
        days, months, and years between two arbitrary dates.
    """
    target1 = datetime.date(2000, 1, 1)
    target2 = datetime.date(2016, 10, 3)

    # dates is a list of dates
    dates = [
        datetime.date(2010, 1, 15),
        datetime.date(2012, 6, 29)
    ]

# loop through each of the dates and compare to the target1 and target2
    for date in dates:
        if target1 > date:
            print('There are', datetimecalculate(target1, date, 'days'), 'days between', target1, 'and', date)
            print('There are', datetimecalculate(target1, date, 'months'), 'months between', target1, 'and', date)
            print('There are', datetimecalculate(target1, date, 'years'), 'years between', target1, 'and', date)

        else:
            print('There are', datetimecalculate(date, target1, 'days'), 'days between', date, 'and', target1)
            print('There are', datetimecalculate(date, target1, 'months'), 'months between', date, 'and', target1)
            print('There are', datetimecalculate(date, target1, 'days'), 'years between', date, 'and', target1)

        # print number of days between date and target11
        if target2 > date:
            print('There are', datetimecalculate(target2, date, 'days'), 'days between', target2, 'and', date)
            print('There are', datetimecalculate(target2, date, 'months'), 'months between', target2, 'and', date)
            print('There are', datetimecalculate(target2, date, 'years'), 'years between', target2, 'and', date)

        else:
            print('There are', datetimecalculate(date, target2, 'days'), 'days between', date, 'and', target2)
            print('There are', datetimecalculate(date, target2, 'months'), 'months between', date, 'and', target2)
            print('There are', datetimecalculate(date, target2, 'days'), 'years between', date, 'and', target2)


def datetimecalculate(date1, date2, flag):
    if flag == 'days':
        if date1 > date2:
            return (date1 - date2).days
        else:
            return (date2 - date1).days

    elif flag == 'months':
        if date1 > date2:
            return int((date1 - date2).days / 30.4)
        else:
            return int((date2 - date1).days / 30.4)

    elif flag == 'years':
        if date1 > date2:
            return int((date1 - date2).days / 365.25)
        else:
            return int((date2 - date1).days / 365.25)

class Test_datetimecalculate(TestCase):

    target1 = datetime.date(2000, 1, 1)
    target2 = datetime.date(2016, 10, 3)

    # dates is a list of dates
    dates = [
        datetime.date(2010, 1, 15),
        datetime.date(2012, 6, 29)
    ]

    def test_datetimecalculate(self):
        for date in Test_datetimecalculate.dates:
            days = datetimecalculate(date, Test_datetimecalculate.target1, 'days')
            months = datetimecalculate(date, Test_datetimecalculate.target1, 'months')
            years = datetimecalculate(date, Test_datetimecalculate.target1, 'years')

            self.assertEqual(datetimecalculate(date, Test_datetimecalculate.target1, 'days'), days)
            self.assertEqual(datetimecalculate(date, Test_datetimecalculate.target1, 'months'), months)
            self.assertEqual(datetimecalculate(date, Test_datetimecalculate.target1, 'years'), years)

 #           days = datetimecalculate(date, Test_datetimecalculate.target2, 'days')
 #           months = datetimecalculate(date, Test_datetimecalculate.target2, 'months')
 #           years = datetimecalculate(date, Test_datetimecalculate.target2, 'years')

  #          self.assertIsInstance(Test_datetimecalculate.target1, datetime.date, 'Parameter Value Should be date type')


if __name__ == '__main__':
    unittest.main(exit=False)
    main()




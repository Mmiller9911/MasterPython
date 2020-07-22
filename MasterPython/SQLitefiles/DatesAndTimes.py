#  ============================================================================================================================================
#  Converting dates and times to utc/local times in a sqlite database:
#  METHOD 1
#  ============================================================================================================================================

import sqlite3
import pytz
import pickle
#  ============================================================================================================================================
#  2020-04-25 10:50:52.652170	2020-04-25 11:50:52.652170+01:00
#  ============================================================================================================================================
# db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
#
# for row in db.execute('select * from history'):
#     # print (row)
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print('{}\t{}'.format(utc_time, local_time))
#
#
# db.close()

#  ============================================================================================================================================
#  Converting dates and times to utc/local times in a sqlite database:
#  METHOD 2
#  ============================================================================================================================================
# use the strftime method of sqlite (this is as OPPOSED to the python strf function)
# provide the format you want the result to be in with the string
# provide a time to use
# provide a modifier eg . 'localtime'
# this is fully explained HERE - https://www.sqlite.org/lang_datefunc.


#  ============================================================================================================================================
#  ('2020-04-25 11:50:52.652', 'John', 1000)
#  ============================================================================================================================================
# db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
#
# for row in db.execute("select strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
#                       " history.account, history.amount FROM history order by history.time"):
#     print(row)
#
# db.close()


#  ============================================================================================================================================
#  2020-04-25 10:50:52.652170	2020-04-25 11:50:52.652170+01:00	GMT Daylight Time
#  ============================================================================================================================================
# db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
#
# for row in db.execute("SELECT * FROM history"):
#     utc_time = row[0]
#     pickled_zone = row[3]
#     zone = pickle.loads(pickled_zone)
#     local_time = pytz.utc.localize(utc_time).astimezone(zone)
#     print('{}\t{}\t{}'.format(utc_time, local_time, local_time.tzinfo))
#     # print(row)
#
# db.close()

#  ============================================================================================================================================

import sqlite3
import datetime
import time
import pickle
import pytz
#  ============================================================================================================================================
# Retrieved record for John. Current balance of account John is 19.40
# 10.00 deposited
# 0.30 withdrawn
# Current balance of account John is 29.10
#  ============================================================================================================================================

db = sqlite3.connect('accounts.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
db.execute('CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)')
db.execute('CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL,'
           ' account TEXT NOT NULL, amount INTEGER NOT NULL, zone INTEGER NOT NULL,'
           ' PRIMARY KEY (time, account))') # this is a composite key
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS "
           "SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history order by history.time")


class Account(object):

    @staticmethod
    def _current_time():
        utc_time = pytz.utc.localize(datetime.datetime.utcnow())
        local_time = utc_time.astimezone()
        zone = local_time.tzinfo
        return utc_time, zone  # we now use a tuple to return multiple values in one return statement

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute('Select name, balance FROM accounts WHERE (name = ?)', (name,))
        row = cursor.fetchone()

        if row is not None:  # this could just be 'row'
            self.name, self._balance = row
            print('Retrieved record for {}. '.format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute('INSERT INTO accounts VALUES (?, ?)', (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {} ".format(self.name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount # dont update actual balance in case the transaction fails
        deposit_time, zone = Account._current_time() # unpack the tuple
        pickled_zone = pickle.dumps(zone)
        db.execute('UPDATE accounts SET balance = ? WHERE (name = ?)', (new_balance, self.name))
        db.execute('INSERT INTO history VALUES (?, ?, ?, ?)', (deposit_time, self.name, amount, pickled_zone))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            self._save_update(amount)
            print('{:.2f} deposited'.format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            self._save_update(-amount)
            print('{:.2f} withdrawn'.format(amount / 100))
            return amount / 100
        else:
            print('amount must be greater than zero and not more than account balance')
            return 0.0

    def show_balance(self):
        print('Current balance of account {} is {:.2f}'.format(self.name, self._balance / 100))


if __name__ == '__main__':
    john = Account('John')
    john.deposit(1000)
    time.sleep(3)
    john.withdraw(30)
    john.show_balance()

    db.close()

 #============================================================================================================================================
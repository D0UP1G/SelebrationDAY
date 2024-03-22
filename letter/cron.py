from django_cron import CronJobBase, Schedule
import sqlite3 as sq3


class Job(CronJobBase):
    RUN_EVERY_MINS = 1 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'letter.cron_job'    # a unique code

    db = sq3.connect('db.sqlite3')

    def do(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT id FROM letter_letter')
        results = cursor.fetchall()
        for row in results:
            print(row[0])
        print('other')
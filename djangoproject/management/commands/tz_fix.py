from django.core.management.base import NoArgsCommand
from django.db import connection, transaction

class Command(NoArgsCommand):
    help="update time zone of every date field"

    def handle_noargs(self, **options):
        cursor = connection.cursor()

        cursor.execute('SHOW tables')
        tables = [t[0] for t in cursor.fetchall()]
        for table in tables:
            query = "DESCRIBE %s" % table
            cursor.execute(query)
            fields = cursor.fetchall()
            for field in fields:
                if field[1] == 'datetime':
                    query = "UPDATE %s SET %s = CONVERT_TZ(%s, 'America/New_York', 'UTC')" % (table, field[0], field[0])
                    cursor.execute(query)
                    transaction.commit_unless_managed()

import random
import datetime
from chat.models import Cigar
def chat_cigar(nrows=5):
    stoppedo = bool(random.getrandbits(1))



    for i in range(nrows):
        start_date = datetime.datetime(2021, 1, 1)
        end_date = datetime.datetime(2021, 3, 20)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.total_seconds()
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(seconds=random_number_of_days)
        print(random_date)
        stoppedo = bool(random.getrandbits(1))
        if stoppedo:
            stoppedo = -1
        else:
            stoppedo = 1
        print(stoppedo)
        Cigar(pub_date=random_date, stopped=stoppedo).save()
#Zadanie 3: Age in Seconds - oblicz swój wiek w sekundach.
#Tu przydatne będzie zaimportowanie date z modułu datetime.
#Pewnym utrudnieniem (chyba) jest poproszenie, aby użytkownik wpisał date swoich urodzin.

import datetime

now=datetime.datetime.now()
print(now)
you=input("When did you birth? (In YYY-MM-DD)\n")
you_date=datetime.datetime.strptime(you,'%Y-%m-%d')
you_date2=you_date.date()
diff=(now-you_date).total_seconds()
print("So your birth date is", you_date2)
print("Wow! You live on the planet Earth for %d seconds now!" % diff)

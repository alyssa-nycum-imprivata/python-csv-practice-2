import csv

f = open('attendees1.csv')
csv_f = csv.reader(f)

attendee_emails1 = []

for row in csv_f:
    attendee_emails1.append(row[2])


f = open('attendees2.csv')
csv_f = csv.reader(f)

attendee_emails2 = []

for row in csv_f:
    attendee_emails2.append(row[2])

attendee_emails1 = set(attendee_emails1)
attendee_emails2 = set(attendee_emails2)

new_attendees = attendee_emails2.difference(attendee_emails1)

for attendee in new_attendees:
    print(attendee)
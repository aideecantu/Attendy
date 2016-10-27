import facebook
import csv
from datetime import datetime

def id_date_dict(group_obj):
	""" Create event id to date dictionary, to write into csv. """
	event_dates = dict()
	for i in group_obj['events']['data']:
		event_id = i['id']
		date_str = i['start_time'].split('T')[0]
		event_dates[event_id] = date_str
	return event_dates

def date_names_dict(event_dates):
	""" See names of students present on that date, from dictionary """
	attendance = dict()
	duplicates = 1
	for event_id in event_dates:
		key = event_dates[event_id]
		if key not in attendance:	
			attendance[key] = set()
		elif key in attendance:
			duplicates += 1
			key = event_dates[event_id] + ' ' + str(duplicates)
			attendance[key] = set()
		# GET tags of photos in event
		event_obj = graph.get_object(id=event_id + '/photos?', fields='tags')
		# some events have no photos yet
		if event_obj['data'] is None:
			continue
		if 'tags' in event_obj['data'][0]: 
			tags = event_obj['data'][0]['tags']['data']
			for tag in tags:
				attendance[key].add(tag['name'])
		elif 'tags' not in event_obj['data'][0]:
			attendance.pop(key)
	return attendance

def collect_all_students(attendance):
	""" Roster with names of all students to write in csv. """
	all_students = set()
	for date in attendance:
		for name in attendance[date]:
			all_students.add(name)
	return all_students

def write_csv(attendance, all_students):
	first_row = ['IEOR 171', 'Attendance']
	date_row = [''] + ['Absences'] + [date for date in sorted(attendance.keys())]
	f = '171_attendy.csv'
	with open(f, 'wt', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(first_row)
		writer.writerow(date_row)
		attendance_dates = sorted(attendance.keys())
		for student in sorted(all_students):
			row = [student]
			tally_row = []
			absences = 0
			for date in attendance_dates:
				if student in attendance[date]:
					tally_row.append('1')
				else:
					absences += 1
					tally_row.append('0')
			row.append(str(absences))
			row += tally_row
			writer.writerow(row)

group_id = input("Please paste your group id (number in the Facebook group's URL): ") 
token = input("Please paste your user access token: ")
graph = facebook.GraphAPI(access_token=token, version='2.7')
group_obj = graph.get_object(id=group_id, fields='events')

event_dates = id_date_dict(group_obj)
attendance = date_names_dict(event_dates)
roster = collect_all_students(attendance)
write_csv(attendance, roster)
print("All done! Check your directory for <171_Attendy.csv>")

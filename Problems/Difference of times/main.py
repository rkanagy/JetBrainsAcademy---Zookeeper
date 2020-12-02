# put your python code here
first_event_hours = int(input())
first_event_minutes = int(input())
first_event_seconds = int(input())
second_event_hours = int(input())
second_event_minutes = int(input())
second_event_seconds = int(input())
first_event_number_of_seconds = first_event_hours * 60 * 60 + first_event_minutes * 60 + first_event_seconds
second_event_number_of_seconds = second_event_hours * 60 * 60 + second_event_minutes * 60 + second_event_seconds
difference_in_seconds = second_event_number_of_seconds - first_event_number_of_seconds
print(difference_in_seconds)

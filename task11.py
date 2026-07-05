#meeting room booking conflict checker
existing_meeting_start=int(input(" existing meeting start time: "))
existing_meeting_end=int(input(" existing meeting end time:"))
new_meeting_start=int(input(" new meeting start time: "))
new_meeting_end=int(input(" new meeting end time: "))

#using comparision and logical opertors ,check conflicts meeting
if (new_meeting_start<existing_meeting_end and new_meeting_end>existing_meeting_start):
    print("Meeting conflict exists.")   
elif (new_meeting_start>=existing_meeting_end or new_meeting_end<=existing_meeting_start):
    print("No meeting conflict.")   
else:
    print("Invalid input.")
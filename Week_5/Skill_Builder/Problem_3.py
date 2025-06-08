registered = set(map(int, input().split()))
attended = set(map(int, input().split()))
dropped_out = set(map(int, input().split()))
registered_and_attended = registered & attended
fnal_students = registered_and_attended - dropped_out
print(registered_and_attended)
print(fnal_students)
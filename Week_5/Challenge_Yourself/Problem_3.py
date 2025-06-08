# You are using Python
# Read input sets
P = set(map(int, input().split())) # Borrowed books
Q = set(map(int, input().split())) # Returned books
R = set(map(int, input().split())) # Added books
S = set(map(int, input().split())) # Missing books
# Step 1: Borrowed but not returned
diff1 = sorted(P - Q, reverse=True)
print(diff1)
# Step 2: Added but now missing
diff2 = sorted(R - S, reverse=True)
print(diff2)
# Step 3: Union of both differences
fnal_union = sorted(set(diff1).union(diff2), reverse=True)
print(fnal_union)
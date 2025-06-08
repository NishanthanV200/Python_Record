# Read size and elements of frst DNA sequence
n = int(input())
seq1 = list(map(int, input().split()))
# Read size and elements of second DNA sequence
m = int(input())
seq2 = list(map(int, input().split()))
# Compare only up to the length of the shorter sequence
min_len = min(n, m)
# Collect matching bases at the same positions
matches = []
for i in range(min_len):
 if seq1[i] == seq2[i]:
  matches.append(str(seq1[i]))
# Output the result
print(" ".join(matches))
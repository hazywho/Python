n,m = 2000, 1277
df = []
with open(r"C:\Users\zanyi\OneDrive\Git hub\Python\MCC\Real\innovation.txt") as f:
    for i in f:
        df.append(list(map(int,i.split(" "))))
# Define a custom function that returns the sum of the first two elements of a row
def sum_first_two(row):
  return row[0] + row[1]
def sum_of_all(row):
  return row[0] + row[1] + row[2] + row[3]

# Sort the data frame by the custom function in descending order
sorted_df = sorted(df,key=sum_first_two,reverse=True)
count = 0
for i in range(m-1):
  print(sorted_df[i])
  count += sum_first_two(sorted_df[i])
  sorted_df.pop()
# Print the sorted data frame
sorted_df = sorted(df,key=sum_of_all,reverse=True)
for i in range(4):
  count+= sorted_df[0][i]

print(count)
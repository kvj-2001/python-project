n = input("Enter the Number:")
if n==n[::-1]:
	print("{}  palimdrome".format(n))
else:
	print("{} is not palimdrome".format(n))
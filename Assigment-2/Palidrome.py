s=input("Enter the input to check :")
sRev=s[::-1]

if s==sRev:
    print(f"Given string {s} is palidrome")
else:
    print(f"Given string {s} is not palidrome")
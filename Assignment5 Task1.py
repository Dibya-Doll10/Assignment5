student = {
    "Alice": "50",
    "John" : "60",
    "Babe" : "70",
    "Sampson" : "80",
    "Harry" : "85"
}
input("Enter the required student's name: ")
try:
   smarks = student.get("Alice")
   print("Alice's marks is ",smarks)
except:
    print("Name not found")
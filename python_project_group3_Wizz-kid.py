EmailId = str(input("Enter Your Email_Id: "))
username = EmailId[:EmailId.index("@")]
print("Your Name is",username ,end=(""))
domain = EmailId[EmailId.index("@") + 1:]
print("\nYour Domain is",domain.upper())
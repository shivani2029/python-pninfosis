user_status: str=input("enter the status")
if user_status=="online":
    print("user is online")
elif user_status=="in call":
    print("user is in call")
elif user_status=="busy":
    print("user is busy")
else:
    print("user is offline")

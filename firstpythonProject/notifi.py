# import win10toast
from win10toast import ToastNotifier

# create an object to ToastNotifier class
n = ToastNotifier()
n.show_toast("GEEKSFORGEEKS", "Notification body", duration=20)
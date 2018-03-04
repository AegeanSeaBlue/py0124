from win10toast import ToastNotifier

toast = ToastNotifier()

for i in range(10):
    toast.show_toast(title='', msg=str(i), duration=2)

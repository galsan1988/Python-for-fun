
#THERE IS A DIVISION BY ZERO but everything works, because we didn't execute this code line
def func1():
    return 1/0




try: 
    func1()
except Exception as e:
    print(f"{e}")
else:
    print ("Executed if no mistake was found")
finally:
    print ("executed anyway")


class SendDataException (Exception):
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"error {self.message}"

class SendUserData:
    def printout(self, data):
        self.send_data(data)
        print(f"printing {str(data)}")

    def send_data (self, data):
        if not self.check_data(data):
            raise SendDataException ("no memory available")

    def check_data(self,data):
        return False

usama = SendUserData()
try:
    usama.printout('nothing else matters')
except Exception as e:
    print(e)
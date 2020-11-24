import threading
import time
import atexit
import os

def account():
  i = 0
  @atexit.register
  def goodbye():
    print ("'CLEANLY' kill sub-thread")
  os.system('py test.py')


def email():
  @atexit.register
  def goodbye():
    print ("'CLEANLY' kill sub-thread")
  os.system('py test.py')

t = threading.Thread(target=account)
t1 = threading.Thread(target=email)
t1.daemon = True
t.daemon = True
t.start()
t1.start()

def after_timeout():
    print("KILL MAIN THREAD: %s" % threading.currentThread().ident)
    raise SystemExit

threading.Timer(2, after_timeout).start()
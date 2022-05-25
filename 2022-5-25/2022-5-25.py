import datetime
import time
import threading
import tkinter as tk


class SampleApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.clock = tk.Label(self,text="")
        self.clock.pack()

        self.update_clock()

    def update_clock(self):
        now = time.strftime("%H:%M:%S",time.localtime())
        self.clock.configure(text = now)
        self.after(1000,self.update_clock)
if __name__ =="__main__":
    app=SampleApp()
    app.mainloop()
# looping = True
#
# prev_callback_time = datetime.datetime.now()
# def callback():
#     global prev_callback_time
#     now = datetime.datetime.now()
#     delta = now-prev_callback_time
#     prev_callback_time = now
#     print(f'{now} ({delta})')
#
# def simple_timer():
#     callback()
#     if looping:
#         threading.Timer(1,simple_timer).start()
#
# #simple_timer()
#
# def simple_timer2():
#     global prev_callback_time
#     prev_delta = datetime.timedelta(0)
#     while looping:
#         now = datetime.datetime.now()
#         delta = now - prev_callback_time + prev_delta
#
#         if delta >= datetime.timedelta(seconds=1):
#             callback()
#             prev_delta = delta - datetime.timedelta(seconds=1)
#             prev_callback_time = now
# simple_timer2()
# def calc():
#     time.sleep(20)
#     print('Done')
#
# thread = threading.Thread(target= calc)
# thread.start()
# print('calc is running')
# def calc():
#     prod = 1
#     for i in range(1,100000):
#         prod*=i
#     print(prod)
# def hello():
#     for i in range(10):
#         print('hello')
#
# start_time = time.time()
# hello()
# end_time = time.time()
#
# print(f'Run for {end_time-start_time} secs.')
#
# import timeit
# timeit.timeit(hello,number=1)
#
# import cProfile
# cProfile.run('calc()')
#
# now = datetime.datetime.now()
# now.strftime('%Y/%m/%d %H:%M:%S')
# now.strftime('%I:%M %p')
# now.strftime('%B of %y')
#
# datetime.datetime.strptime('August 22,1970','%B %d,%Y')
# datetime.datetime.strptime('2021/08/22 13:29:00','%Y/%m/%d %H:%M:%S')
# datetime.datetime.strptime("August of '70","%B of '%y")

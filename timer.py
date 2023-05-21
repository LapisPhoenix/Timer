#!/usr/bin/env python3

from plyer import notification
from colorama import Fore, Style, init
from playsound import playsound
from time import sleep
from argparse import ArgumentParser
import threading
import sys
import os



class Timer:
    def __init__(self):
        # colorama
        init()

        # argparse
        self.parser = ArgumentParser()
        self.parser.add_argument("-H", "--hours", type=int, default=0)
        self.parser.add_argument("-m", "--minutes", type=int, default=0)
        self.parser.add_argument("-s", "--seconds", type=int, default=0)
        self.parser.add_argument("-t", "--title", type=str, default="Timer")
        self.parser.add_argument("-d", "--description", type=str, default="Timer is done!")
    

    def start(self):
        # argparse
        self.args = self.parser.parse_args()
        if len(sys.argv) == 1:
            self.parser.print_help(sys.stderr)
            sys.exit(1)

        self.hours = self.args.hours
        self.minutes = self.args.minutes
        self.seconds = self.args.seconds
        self.title = self.args.title
        self.description = self.args.description

        # start timer
        self.timer()


    def alarm():
        playsound(f"{os.path.dirname(os.path.realpath(__file__))}/alarm.mp3")    


    def timer(self):
        self.total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        
        if self.total_seconds < 0:
            print(f"{Fore.RED}[-] {Style.RESET_ALL}Time can't be negative.")
            sys.exit(1)
        elif self.total_seconds == 0:
            self.total_seconds += 1
        

        while self.total_seconds:
            self.hours, self.minutes = divmod(self.total_seconds, 3600)
            self.minutes, self.seconds = divmod(self.minutes, 60)
            self.time = f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"
        
            print(f"{Fore.GREEN}[{self.time}] {Style.RESET_ALL} Time Left.", end="\r")
        
            sleep(1)
            self.total_seconds -= 1
        
        print(f"{Fore.GREEN}[00:00:00] {Style.RESET_ALL}{self.description}")
        
        notification.notify(
            title=self.title,
            message=self.description,
            app_icon=f"{os.path.dirname(os.path.realpath(__file__))}/alarm.ico",
            timeout=15
        )
        
        threading.Thread(target=Timer.alarm).start()


if __name__ == "__main__":
    timer = Timer()
    timer.start()
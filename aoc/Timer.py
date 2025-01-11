import time
import importlib

class TimerError(Exception):
    "Error in Timer class!"

class Timer:
    def __init__(self, text="{1} miliseconds.", logger=print):
        self._start_time = None
        self.text = text
        self.logger = logger

    def tic(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .toc() to stop it")
        self._start_time = time.perf_counter()

    def toc(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .tic() to start it")
        
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        if self.logger:
            self.logger(self.text.format(elapsed_time))
        return elapsed_time * 1000
    
    def timing_handeler(self, func):
        """calls the function on () and counts the time of execution. Returns the output of the function and the execution time."""
        self.tic()
        _ = func()
        time = self.toc()
        return time

def showAndTell(times):
    hat = ' ' + '+' * 100 + '\n'
    line = ' ' + '+' * 100 + '\n'
    out = hat + f"|{"": ^10}|{"partie 1": ^44}|{"partie 2": ^44}|\n" + line
    for day, time in enumerate(times):
        if type(time) == tuple:
            out += f"|{f"jour {day+1}": ^10}|{f"{time[0]:.4f}ms": ^44}|{f"{time[1]:.4f}ms": ^44}|\n"
        else:
            out += f"|{f"jour {day+1}": ^10}|{f"{time:.4f}ms": ^89}|\n"
        out += line
    return out

def main():
    t=Timer(logger=False)
    times = []
    for i in range(1, 26):
        try:
            day = importlib.import_module(f"2024.{i}.jour{i}")
            s = day.Solution(day.__file__[:-2] + "txt")
            if hasattr(s, "partie1"):
                t1 = t.timing_handeler(s.partie1)
                t2 = t.timing_handeler(s.partie2)
                times.append((t1, t2))
            else:
                t0 = t.timing_handeler(s.partie12)
                times.append(t0)
        except:
            print(f"error while executing file of day {i}.")
    print(showAndTell(times))

if __name__ == "__main__":
    main()

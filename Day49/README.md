### Day 49!

Today is about measuring performance using [cprofile](https://docs.python.org/3/library/profile.html).

syntax for overall test: python -m cProfile -s cumtime program.py

cProfile can also be added to a specific block in the code iteslf.  

import cProfile
profiler = cProfile.ProFile()
profiler.disable()

find your section that you want to measure....

profiler.enable()
method1()
method2()
profiler.disable

profiler.print_stats(sort='cumtime')
 

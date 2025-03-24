#Asher Wangia, Debugging Notes
import trace
import sys

def trace_calls(frame, event, arg):
    if event == 'call': #when the function is called
        print(f'Calling function: {frame.f_code.co_name}')
    elif event == 'line': #when a new line of code happens
        print(f'Executing line {frame.f_lineno} in {frame.f_code.co_name}')
    elif event == 'return': #when we return stuff
        print(f'{frame.f_code.co_name} returned {arg}')
    elif event == 'exeception': #Triggered when there is an exception
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)
tracer = trace.Trace(count=False, trace=True)

#1. What is tracing?
def sub(numone, numtwo):
    return numone - numtwo

def add(numone, numtwo):
    print(sub(numone, numtwo))
    return numone + numtwo


print(add(5,2))

tracer.run('add(8,9)')
#Basic Trace command
    # python -m trace --trace Notes\tracing.py
"""
    --trace(display lines as executed)
    --count(display number of time executed)
    --listfuncs(display functions used in program)
    --tracecalls(displays relationships between functions)
"""
#2. What are some ways we can debug by tracing?
    #Lets you observe what your program is doing without interupting it

#3. How do you access the debugger in VS Code?
    #click the debugger on the left
    #F5 key
    #drop down next to run button

#4. What is testing?
    #running your code to make sure it works as required, trying to break it

#5. What are boundary conditions?
    #Check the entries most likely to be wrong


#6. How do you handle when users give strange inputs?
    #Use conditionals
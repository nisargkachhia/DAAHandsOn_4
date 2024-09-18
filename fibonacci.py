# Fibonacci function implementation with tracing
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Function to track the call stack of Fibonacci calls
def fib_with_trace(n, call_stack=None):
    # Initialize the call stack if it's the first call
    if call_stack is None:
        call_stack = []
    
    # Add the current function call to the stack
    call_stack.append(f'fib({n})')
    
    # Base cases: return the result for n == 0 or n == 1 along with the call stack
    if n == 0:
        return 0, call_stack
    elif n == 1:
        return 1, call_stack
    else:
        # Recursive case: break down the problem into smaller Fibonacci calls
        fib_n1, call_stack = fib_with_trace(n - 1, call_stack)
        fib_n2, call_stack = fib_with_trace(n - 2, call_stack)
        # Return the sum of the two Fibonacci numbers along with the updated call stack
        return fib_n1 + fib_n2, call_stack

# Now let's call the traced Fibonacci function for fib(5) and display the results
result, call_stack = fib_with_trace(5)

# Display the call stack and result
print("Recursive Call Stack Trace:")
for call in call_stack:
    print(call)
    
print("\nResult of fib(5):", result)

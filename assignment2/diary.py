import traceback # Task 1
try:
    with open('diary.txt', 'a') as diary:
        first = True
        while True:
            if first:
                user_entry = input('What happened today? ')
                first = False # Every loop after uses the else:
            else:
                user_entry = input('What else? (type "done for now" to finish) ')
            diary.write(user_entry + '\n') # Append input and add a newline to each entry. Include termination line
            if user_entry.lower() == 'done for now': # Calling .lower() prevents from entering termination twice
                break # Stop when user enters 'done for now'
except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message: 
        print(f"Exception message: {message}")
    print(f'Stack trace: {stack_trace}')
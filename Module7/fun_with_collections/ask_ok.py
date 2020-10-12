def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print("debug")
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            #return False
            retries = retries - 1
            print(retries)
            if retries < 0:
             raise ValueError('invalid user response')
        
            print(reminder)
            return reminder

    #if retries < 0:
        #raise ValueError('invalid user response')
    #print(reminder)

if __name__ == '__main__':
    #ask_ok('Do you really want to quit?')
    ask_ok('OK to overwrite the file?', 2)
    #ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
    #ask_ok(reminder= 'Come on, only yes or no!', prompt='OK to overwrite the file?', )



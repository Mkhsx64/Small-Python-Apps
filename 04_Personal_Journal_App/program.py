
def main():
    print_header()
    run_event_loop()


def print_header():
    print('------------------------------')
    print('        JOURNAL APP')
    print('------------------------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    
    cmd = None
    while cmd != 'x':
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()    
        if cmd == 'l':
            print("L")
        elif cmd == 'a':
            print("A")
        elif cmd != 'x':
            print("Sorry, we don't understand '{}'".format(cmd))

main()

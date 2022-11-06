while True:
    try:
        x = float(input('Enter a num: '))
    except ValueError:
       print('Caught exception')
    else:
        print('Entered succesfully')
        break
    finally:
        print('This part will be written anyway')
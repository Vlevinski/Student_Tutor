# How to handle exceptions in Python

use statementslike:
    *try:
        # what you do
    except < exception> as e:
        # check exception
        raise e*

full check:
    *try:
        print('I am sure no exception is going to occur!')
    except Exception:
        print('exception')
    else:
        # any code that should only run if no exception occurs in the try,
        # but for which exceptions should NOT be caught
        print('This would only run if no exception occurs. And an error here '
              'would NOT be caught.')
    finally:
        print('This would be printed in every case.')*

.

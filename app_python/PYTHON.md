# DevOps lab 1-2
## Lab 1
I developed a Python web application, that shows current time in Moscow (the code you can see in file main.py).

The best practices that I used:  
1. Flask - web development application.
2. Gunicorn - a Python WSGI HTTP Server for UNIX, that is used for my app on production stage.
3. .gitignore file
4. requirements.txt file to provide all dependences that are used
5. Using popular linter flake8
6. Using Docker containers to containerize app

## Lab 3
Add unit test for my web application.

The best practices that I used:
1. A testing units focus on one tiny bit of functionality and prove it correct.  
2. Using long and descriptive names for testing functions.
3. Test don't Duplicate Implementation Logic
4. Using assert pattern to clearly define the phases of test case
5. Test are isolated (The test are not be able to influence other tests.)

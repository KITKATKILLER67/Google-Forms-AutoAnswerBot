# Google-Forms-AutoAnswerBot
An auto-answering bot for Google Forms (one question long only rn) that is fully customizable, and is very speedy!
**Does not work when e-mails are required**

# SYSTEM REQUIREMENTS:

Python3: 
  Download at {https://www.python.org/downloads/release/python-3115/}

Selenium:
  After installing Python3, open the command line in Windows with administrator privileges, then type >>pip install selenium
  You should be good to go!

CPU:
  I would recommend a beefier CPU, as one instance can be quite bulky, and running several instances of this program for maximum voting can cast a heavy toll on your CPU.
  Tip: Use multiple computers for more voting capabilities!

RAM:
  Minimum: 4 Gigabytes DDR3
  Recommended: 16 Gigabytes DDR4
  For Best Results: 524288 Gigabytes DDR7 (Don't have that much? Don't worry, you'll likely be okay with what you have)

Everything else in a computer:
  Meh

# HOW TO CUSTOMIZE YOUR NEW PYTHON PROGRAM

After you have installed Python3, Selenium, and have downloaded the program, you must customize it for your benefit (and so it works to your advantage lol).

There are three things you must change in the program before it can work.
First, replace <YOUR CHOSEN GOOGLE FORM> (angle brackets included) with your Google form link.
It should look like this <https://docs.google.com/forms/d/e/ThisIsAFormIDAndItIsUsuallyReallyLong/viewform>
Put that link where the <YOUR CHOSEN GOOGLE FORM> is (don't forget to remove the angle brackets!)

Next is the hard part. When you open the form to select your answer choice, right-click on the button and find the div id (LIKE THIS) -> ![image](https://github.com/KITKATKILLER67/Google-Forms-AutoAnswerBot/assets/58996262/1854e7de-8e64-429f-9fa1-14b3f40ea0a0)

Find the div id (in this case it is i8
and put it in the place of <DIV ID> in both spots

Don't forget to remove the angle brackets


# And you're done!

Now save it to an easy spot where you can find it, copy the path of the file, and run it in the cmd line with this command:

It should look like this

C:\Users\yourname> python "C:\Users\yourname\Desktop\file.py"

Above is an example, it might not look exactly like that


# IF YOU HAVE ANY ISSUES PLEASE FILE BUG REPORT I WILL DO MY BEST TO ANSWER THEM

# latest file is v2.0.1

# practice_programs
a grouping of small python programs and projects to practice a variety of fundamentals
will be throwing a variety of simple to more complex miscellaneous python programs and projects into this.

The first is a simple program that will send an email through gmail. It works perfectly and only needs a second confidential file that provides the sender, the receiver, the subject and body of the email, and the app password. super simple stuff.

the word_replacement is an extremely simple starter program that just has a phrase and allows you to choose a word to replace and what to replace it with.

the calculator app i created I improved upon. Often when you see basic little calculator program tutorials on youtube, they wont include exponents and they won't have a handling for dividing by zero. I added both of those into it with an exponent function and a try/except block for dividng by zero.

the email_slicer is also extremely basic and just cuts an email into a domain, username, and extension.

the binary_search was interesting as I had never looked into the logic of how it works. I want to test it on much larger data to see just how much faster it can be.

Both the QR code generator and the interest calculator are very simple implementations. The QR code specifically I thought would be a lot more difficult, but I was able to import in the package qrcode which really takes care of most of it for you.

The password_generator uses the random module of course and it is another I ended up improving from the youtube video I was following along with. It did not originally have any way to handle exceptions if someone entered something wrong in the input but I added that in as a failsafe.

The quiz wasn't anything special, although it is something I want to go back and flesh out more. the implementation is just a for loop going through a dictionary and keeping track of correct answers.

The video I was learning from made a very basic dice roller that would roll 2 d6's and show a visual of what was rolled. I was not happy with this at all and drastically altered it. For one, I dropped the visual because I didn't find it necessary. Then, I altered the program so that it could roll a d4, d6, d8, d10, d12, d20, or a d100. Lasstly, I added an exception block that was shockingly missing from the original program to make sure nobody could break the program by entering in something other than the inputs specified.

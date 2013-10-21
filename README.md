This is a pythonic implementation of Andrew Ng's Coursera course on machine learning.

I'll be doing the course as close to real-time as possible (won't be rushing ahead but shouldn't fall behind) and writing as much as possible/I deem necessary in Python. 

You'll notice I've skipped the calculations of matrix inverses and transposes from the optional material (well, that's very presumptious of me, you might not have noticed) - I've decided that I'm happy to rely on existing implementations for that stuff.

I'll obviously have to make decisions around what I'm happy to borrow and what I want to implement myself but if anybody wants to add these things, please feel free!

Any questions, please direct to matthewsharpe3@gmail.com


## To-do

Would love to add real time graph updates to show the cost function varying with time along with the changing straight line guesses. Rumour has it that matplotlib is the way but I obviously haven't done that yet. -- Have now done this, shows I've got some fairly major problems. Currently the most likely candidate is the calculation of the partial derivatives. I've derived these by hand and they look legit, currently investigating my (supposed) understanding of the zip function and list comprehension.

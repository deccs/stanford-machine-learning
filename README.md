This is a pythonic implementation of Andrew Ng's Coursera course on machine learning.

I'll be doing the course as close to real-time as possible (won't be rushing ahead but shouldn't fall behind) and writing as much as possible/I deem necessary in Python. 

You'll notice I've skipped the calculations of matrix inverses and transposes from the optional material (well, that's very presumptious of me, you might not have noticed) - I've decided that I'm happy to rely on existing implementations for that stuff.

I'll obviously have to make decisions around what I'm happy to borrow and what I want to implement myself but if anybody wants to add these things, please feel free!

Any questions, please direct to matthewsharpe3@gmail.com


## To-do

-- Would love to add real time graph updates to show the cost function varying with time along with the changing straight line guesses. Rumour has it that matplotlib is the way but I obviously haven't done that yet.

-- Have now done this, shows I've got some fairly major problems. Currently the most likely candidate is the calculation of the partial derivatives. I've derived these by hand and they look legit, currently investigating my (supposed) understanding of the zip function and list comprehension.

-- Turned out, the problem was in my shoddy use of integers and floats, am now using ints in all the right places (rarely) and floats wherever I should. There's still a problem with the termination of iteration, maintaining hope that in future lectures this'll be covered (I'll look at it again if it isn't by the end of this week's lectures). Also, can very clearly see how important the learning rate is!

-- Termination of iteration taken care of - just needed to remember what we were doing in the first place, minimizing the cost function! Have set a lower limit on that value, now there are only 2 things I can see to do...

-- Work out how to properly set the learning rate, am going to move ahead in the lectures and see if this is covered.

-- Work out why, if I'm going to converge, I always get the gradient almost immediately and then work my way towards the intercept. I've only noticed this because of graphing it but it's very odd. As an initial thought - I reckon that, as the cost function multiplies the gradient partial derivative term (theta_1) by the training input value (x(i)) and takes absolute values of difference, that by only using integer |x| >= 1 I've caused this. When trying to minimize, as there are multiplicative effects the sum in the partial derivative term for theta_1 will be bigger and so fixing this will be more beneficial in minimizing the error function than fixing the intercept


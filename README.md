# HW2-socioeconomici-correlation-with-affordable-housing
The goal of this study:  
In this analysis, I am trying to address the issue between whether there is a correlation between socioeconomic index and the number of affordable housing in Chicago area. 
To be specific, I will use a censor data from 2008-2012 regarding economic situation to compare another data from 2012-2015 regarding the unit number of affordable housing program. 

Appraoch of the problem: 
1. Declaration: I spent more time to get the data structure I want, and I am still weak at this. However, given this is my first programming practice, I feel like I learned a lot by reading tutorial and discuss with other students.
2. I could not figure out how to combine data by coding, so I had to manually do something before I can desperately not finish the project. 
3. After combining data in one sheet, I found there are some areas missing on that sheet, so I created two sets and found the difference and manually add the missing areas into that sheet, with 0 for the parameter. 
4. After creating a new csv file with the same length and same order (probably I should leave this for coding, with a dictionary function and sorting, but next time) I created two lists containing income and number of affordable housing units in the same order and same length. 
5. I put these two lists into a scipy pearsonr test and got the r and p
6. I tried to do the unit test for my parsing data by confirming the length of my list is what i want, I also attempted to test the pearsonr test by choosing some known list and result

Conclusion: 
with r=0.19795112500667397 and p=0.084397024355638312, it is unlikely there is a correlation between income and the number of affordable housing in the area. In other words, when you go to an neighborhood with more affordable housing units, it does not imply this is a low income area based on the current results.


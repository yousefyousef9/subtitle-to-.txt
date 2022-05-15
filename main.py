TEXT = """
1

00:00:00,510 --> 00:00:08,580

as we discussed in the previous lectures, we need to know about math or mathematics, physics



2

00:00:08,760 --> 00:00:15,480

and also python programming language in order to understand the quantum computers in a much better way.



3

00:00:15,960 --> 00:00:18,630

So that's what we're going to start with in this lecture.


"""

TEXT_NEW = ""

for x in TEXT :
	
	if (x.isalpha() or x == " ")  :
		TEXT_NEW = TEXT_NEW + x ;

text_file = open("data.txt", "w")
 
text_file.write(TEXT_NEW)
 
text_file.close()

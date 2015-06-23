# Asmt3
# Nathan Richgels

# Data Objects
# DNAStrand- str- The DNA strand that the user enters.
# reverted- str- The DNA segment that the user 
# inverted- str- reverted backwards.
# Mutation- str- The first instance of Mutation is what's inbetween the equivalent of
#reverted and Mutation0 as a single string.  The second instance is the string of
#Mutation0 reversed (esentially the mutated gene).
# Mutation0- str- The sub-string that's between reverted and inverted within the user's DNA strand.
# MDNAStrand- Mutated DNA Strand.

# Welcome the User!
print "Hello!  This program will show you a sample of a substring of DNA that's reversed"
print "between an inverted pair!"

# Request from the user a DNA sequence.
DNAStrand=raw_input("Enter in a DNA strand that contains an inverted pair: ")
print " "

# Ask the user for a pattern within the DNA that will be inverted.
reverted=raw_input("Now enter in the first segment of the inverted pair: ")
print " "

# Now create a reversed version of reverted, or inverted.  I honestly don't understand this operation,
#but my book told me it would reverse a string.
inverted=reverted[::-1]


# "segment out" the segment between the reverted and inverted segment.
Mutation=DNAStrand[DNAStrand.index(reverted):DNAStrand.index(inverted)]

# Remove the remnants of reverted from the string.
Mutation0=Mutation.strip(reverted)

# Reverse the pattern between the noninverted and inverted sequence.
Mutation=Mutation0[::-1]

# Replace the pattern between the noninverted and inverted sequence with the now mutated part of the
#DNA Strand.
MDNAStrand=DNAStrand.replace(Mutation0, Mutation)
print "And your Mutated DNA Strand is: " + MDNAStrand

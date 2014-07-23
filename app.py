# Dictionary of musical notes. The key is name of the note, the value is a zero-based numerical index
notes = {'C':0, 'C#':1, 'D':2, 'D#':3, 'E':4, 'F':5, 'F#':6, 'G':7, 'G#':8, 'A':9, 'A#':10, 'B':11}

# The reverse of notes, such that integer index is key and note name is value
indices = dict((v, k) for k, v in notes.iteritems())

# Dictionary of major keys. The key is the name of the musical key, the value is a set of notes in that key, mapped to the dictionary above
keys = {'C Major': {0,2,4,5,7,9,11}, 'G Major': {0,2,4,6,9,11}, 'D Major': {1,2,4,6,7,9,11}, 'A Major':{1,2,4,6,8,9,11}, 'E Major': {1,3,4,6,8,9,11}, 'B Major':{1,3,4,6,8,10,11}, 'F# Major':{1,3,5,6,8,10,11}, 'C# Major':{0,1,3,5,6,8,10}}

# Accepts notes from the terminal
# Returns a set of notes as strings that are valid keys of the notes dictionary.
def ReadNotesFromStdIn():
	print ('')
	print ('Enter a note (C, C#, D, D#, E, F, F#, G, G#, A, A#, or B).')
	print ('Press the Enter key when you\'re finished')

	sequence = set()
	while True:
		note = raw_input('>')

		if note in notes:
			# valid note - add it to a set of all notes
			sequence.add(note)
		elif note == '':
			# that's all the notes
			break
		else:
			# not a note
			print ('The allowed notes are C, C#, D, D#, E, F, F#, G, G#, A, A#, and B.')
			print ('Press the Enter key when you\'re finished')

	print ('You entered the notes ' + ','.join(sequence))
	return sequence

# Determines the possible keys that a set of notes belongs to
# Returns a set of possible keys
def DetermineKeyFromNotes(sequence):
	# TODO: determine the key
	noteIndices = set()
	for n in sequence:
		noteIndices.add(notes[n])

	print ('Note indices are ' + ','.join(str(i) for i in noteIndices))

	possibleKeys = set()
	for keyName, keyNotes in keys.iteritems():
		if noteIndices <= keyNotes:
			possibleKeys.add(keyName)

	return possibleKeys


# Program entry
print ('Welcome to Fretboard')

while True:
	print ('')
	print ('Select an action to perform:')
	print ('1) Determine a musical key by entering a series of notes')
	print ('2) Exit')
	action = raw_input('>')

	if action == '1':
		# user wants to enter some notes
		sequence = ReadNotesFromStdIn()
		possibleKeys = DetermineKeyFromNotes(sequence)

		print ('Possible keys are: ')
		for k in possibleKeys:
			print (k + ' (' + ','.join(indices[i] for i in keys[k]) + ')')

	elif action == '2':
		# exit the loop, ending the program
		break
	else:
		print ('Unrecognized option')
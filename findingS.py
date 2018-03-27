class FindingS():

	#INITIALIZE THE CLASS WITH THE INPUT OF OUTCOME AND TRAINING ATTRIBUTE LIST
	def __init__(self,positive_outcome,no_of_attributes,result_list,attribute_list):
		#FIND OUT WHAT IS LISTED AS AN POSITIVE OUTCOME
		self.positive_outcome = positive_outcome
		#INITIALIZE THE RESULT LIST, ATTRIBUTE LIST AND THE LENGTH OF THE DATASET TO BE TRAINED UPON
		self.result_list = result_list
		self.attribute_list = attribute_list
		self.training_set_len = len(result_list)
		self.attribute_len = no_of_attributes
		#INITIALIZE EMPTY HYPOTHESIS LIST
		self.hypothesis = []

	#CREATE THE TRAINING METHOD
	def trainS(self):
		#INITIALIZE THE MOST SPECIFIC HYPOTHESIS
		for i in range(0,self.attribute_len):
			self.hypothesis.append(0)
		#START TRAINING
		#LOOP THROUGH THE TRAINING 
		for x in xrange(0,self.training_set_len):
			if self.result_list[x] == self.positive_outcome :
				#ITERATE FOR ALL THE ATTRIBUTE
				for attr in xrange(0,len(self.hypothesis)):
					#CHECK WHAT THE ATTRIBUTE IS 
					#IF IT IS 0 (WHICH IS NULL) THEN UPDATE IT TO THE TRAINING SET SINCE IF THE TRAINING SET CAN CONTAIN A MORE THAN EQUAL GENERAL ATTRIBUTE
					if self.hypothesis[attr] == 0:
						self.hypothesis[attr] = self.attribute_list[x][attr]

					#IF THE HYPOTHESIS ATTRIBUTE IS NOT 0 THEN CHECK IF THEY ARE SAME IF NOT THEN GENERALIZE IT TO "?"
					else :
						if self.hypothesis[attr] != self.attribute_list[x][attr]:
							self.hypothesis[attr] = "?"
						else :
							continue
			else :
				continue

	def resultS(self,attributes):
		#COMPARE THE ATTRIBUTES AND FIND THE RESULT
		for i in range(0,self.attribute_len):
			#COMPARE ALL THE ATTRIBUTES 
			#CHECH IF THE HYPOTHESIS IS GENERIC - "?"
			if self.hypothesis[i] == "?":
				continue
			else :
				if self.hypothesis[i] != attributes[i]:
					return(0)

		return(1)




#Example
s = FindingS(1,3,[1,0,1],[[4,5,6],[2,7,4],[9,6,4]])
s.trainS()
from SortAlgorithm import SortAlgorithm

class JSort(SortAlgorithm):
	"""
    Implements JSort.
	http://home.westman.wave.ca/~rhenry/sort/src/JSortAlgorithm.java
    """

	def sort(self):
		yield
		for x in self.jsort(len(self.items.items) - 1):
			yield

	def jsort(self, length):
		for i in range(length, -1, -1):
			self.reheap(length , i)
		yield
		for i in range(length , -1, -1):
			self.invreheap(length , i)
		yield

		iMarker = self.markers.addMarker(True, 0, (255, 0, 0))
		for i in range(1, len(self.items.items)):
			self.markers.moveMarker(iMarker, i+1)
			yield
			j = i - 1
			jMarker = self.markers.addMarker(False, j, (255, 159, 0))
			while self.cmp.gte(j, 0) and self.cmp.gtI(j, j+1):
				self.items.swap(j, j+1)
				yield
				j -= 1
				self.markers.moveMarker(jMarker, j)
				yield
			self.markers.removeMarker(jMarker)
		self.markers.removeMarker(iMarker)
		yield
	
	def reheap(self, length, i):
		done = False
		temp = self.items.items[i]
		parent = i
		child = 2*(i+1) - 1

		while ((child < length) and not(done)):
			yield
			if (child < length - 1):
				if (self.cmp.gte(self.items.items[child],self.items.items[child+1])):
					child += 1
			if(self.cmp.lt(temp,self.items.items[child])):
				done = True
			else:
				self.items.items[parent] = self.items.items[child]
				parent = child
				child = 2*(parent + 1) -1;
				yield
		self.items.items[parent] = temp

	def invreheap(self,length,i):
		done = False
		temp = self.items.items[length - 1 - i]
		parent = i
		child = 2*(i+1) - 1
		while (child < length and not(done)):
			yield
			if (child < length - 1):
				if (self.cmp.lte(self.items.items[length - 1 - child],self.items.items[length - 1 - (child + 1)])):
					child += 1
			if(self.cmp.gt(temp,self.items.items[length - 1 - child])):
				done = True
			else:
				self.items.items[length - 1 - parent] = self.items.items[length - 1 - child]
				parent = child
				child = 2*(parent + 1) -1;
				yield
		self.items.items[length - 1 - parent] = temp
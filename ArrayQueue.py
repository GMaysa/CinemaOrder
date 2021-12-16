class ArrayQueue:
	def __init__(self):
		self._data = []
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size()

	def is_empty(self):
		return self._size == 0

	def enqueue(self, e):
		self._data.append(e)
		self._size = self._size + 1

	def deque(self):
		if self.is_empty():
			raise Empty('queue is empty')
		else:
			value = self._data[self._front]
			self._data[self._front] = None
			self._front = self._front + 1
			self._size = self._size - 1
			return value

	def first(self):
		if self.is_empty():
			raise Empty('queue is empty')
		else:
			return self._data[self._front]

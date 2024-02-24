class Calculadora:

	def __init__(self):
		self._soma = 0.0
		self.estado = False

	def liga (self):
		self.estado = True

	def desliga (self):
		self.estado = False
		self._soma = 0.0

	def soma (self, valor):
		if self.estado == True:
			self._soma += valor

	def get_soma (self):
		if self.estado == True:
			return self._soma

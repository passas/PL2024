class Calculadora:

	def __init__(self):
		self._soma = 0.0
		self.estado = False

	def liga (self):
		self.estado = True

	def desliga (self):
		self.estado = False
		#self._soma = 0.0

	def soma (self, valor):
		if self.estado == True:
			self._soma += valor

	def get_soma (self):
		return self._soma

	def get_estado (self):
		return self.estado

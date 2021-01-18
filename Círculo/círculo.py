class Círculo():
	def __init__(self, raio=1.00, um='cm'):
		"""Inicializa os próprios atributos."""
		self.raio = raio
		self.um   = um
		
	def __str__(self):
		"""Retorna a descrição da classe."""
		return f'Este é um círculo de raio {self.raio} {self.um}.'
		
	def __repr__(self):
		"""Retorna a representação da classe."""
		return f'Círculo(raio={self.raio:.2f}, um="{self.um}")'
		return
		
	def diâmetro(self, precisão=2):
		"""Retorna do diâmetro do círculo."""
		return str(float(round(self.raio * 2, precisão))) + ' ' + self.um
		
	def circunferência(self, precisão=2):
		"""Retorna a circunferência do círculo."""
		from math import pi
		return str(float(round(2 * pi * self.raio, precisão))) + ' '+ self.um
		
	def área(self, precisão=2):
		"""Retorna a área do círculo."""
		from math import pi
		return str(float(round(pi * (self.raio ** 2), precisão))) + ' ' + self.um + '²'


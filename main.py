# Guilherme Azambuja — 149 429
# Função para inserir um nó na árvore
# Função para remover um nó da árvore
# Função para buscar nó
# Função para imprimir as informações dos nós
# Opção de escolher a categoria de caminhamento (central, pré-fixado, pós-fixado (esquerda e direita)
# Código que testa as funcionalidades

class No:
	def __init__(self, info):
		self.info = info
		self.esq = None
		self.dir = None


class ArvoreBinaria:
	def __init__(self, nome='-----'):
		self.nome = str(nome)
		self.raiz = None
		self.direcoes = {
			'esq',
			'dir'
		}
		self.caminhamentos = {
			'c': None,
			'pr': None,
			'po': None
		}
		self.nomecaminhamentos = {
			'c': 'central',
			'pr': 'pré-fixado',
			'po': 'pós-fixado'
		}
		self.nomedirecoes = {
			'esq': 'esquerda',
			'dir': 'direita'
		}

	def percorrer(self, func, caminhamento, direcao, func_dev=None):

		def central(aux):
			if aux is not None:
				resultado = central(getattr(aux, direcao))
				if resultado is not None:
					return resultado

				resultado = func(aux)
				if resultado is not None:
					return resultado

				resultado = central(getattr(aux, direcao_oposta))
				if resultado is not None:
					return resultado
			else:
				return None

		def prefixado(aux):
			if aux is not None:
				resultado = func(aux)
				if resultado is not None:
					return resultado

				resultado = prefixado(getattr(aux, direcao))
				if resultado is not None:
					return resultado

				resultado = prefixado(getattr(aux, direcao_oposta))
				if resultado is not None:
					return resultado
			else:
				return None

		def posfixado(aux):
			if aux is not None:
				resultado = posfixado(getattr(aux, direcao))
				if resultado is not None:
					return resultado

				resultado = posfixado(getattr(aux, direcao_oposta))
				if resultado is not None:
					return resultado

				resultado = func(aux)
				if resultado is not None:
					return resultado
			else:
				return None

		setattr(
			self,
			'caminhamentos',
			{
				'c': central,
				'pr': prefixado,
				'po': posfixado
			}
		)

		if caminhamento in self.caminhamentos.keys():
			if direcao in self.direcoes:
				if func_dev is not None:
					func_dev()
				direcao_oposta = self.direcoes.copy()
				direcao_oposta.discard(direcao)
				direcao_oposta = direcao_oposta.pop()
				return self.caminhamentos[caminhamento](self.raiz)

			else:
				raise ValueError(f"'{direcao}' Inválido. Parâmetro 'direcao' deve ser {self.direcoes}")
		else:
			raise ValueError(
				f"'{caminhamento}' é inválido. Parâmetro 'caminhamento' deve ser {set(self.caminhamentos.keys())}")

	def imprimir(self, caminhamento='pr', direcao='esq'):

		def anuncio():
			return print(
				f"Impressão da árvore por caminhamento {self.nomecaminhamentos[caminhamento]} à {self.nomedirecoes[direcao]}"
			)

		def imprimir_wrapper(aux):
			return print(aux.info, end=" ")

		param = {
			'func': imprimir_wrapper,
			'func_dev': anuncio,
			'caminhamento': caminhamento,
			'direcao': direcao
		}

		return self.percorrer(**param)

	def buscar(self, info_buscada, caminhamento='pr', direcao='esq'):

		def comparar(aux):
			if aux.info == info_buscada:
				return aux
			else:
				return None

		param = {
			'func': comparar,
			'caminhamento': caminhamento,
			'direcao': direcao
		}

		return self.percorrer(**param)

	def inserir(self, info, info_antecessor=None, direcao=None):
		elemento = No(info)

		if self.raiz is None:
			self.raiz = elemento
			print(f"Elemento '{elemento.info}' adicionado - raíz da árvore '{self.nome}'")

		elif self.raiz is not None and info_antecessor is not None:
			if direcao in self.direcoes:
				elemento_antecessor = self.buscar(info_antecessor)
				if elemento_antecessor is not None:
					espaco_alvo = getattr(elemento_antecessor, direcao)
					if espaco_alvo is None:
						setattr(elemento_antecessor, direcao, elemento)
						print(f"Elemento '{elemento.info}' adicionado - {self.nomedirecoes[direcao]} de '{info_antecessor}'")

					else:
						raise ValueError(f"Posição {self.nomedirecoes[direcao]} do nó '{info_antecessor}' já ocupada")
				else:
					raise ValueError(f"Nó '{info_antecessor}' não encontrado na árvore '{self.nome}'")
			else:
				raise ValueError(f"'{direcao}' é inválido. Parâmetro 'direcao' deve ser 'esq' ou 'dir'")
		else:
			raise ValueError("Parâmetro 'info_antecessor' é necessário")

	def remover(self, info_apaga):

		def achar_antecessor(aux):
			if aux.esq is not None:
				if aux.esq.info == info_apaga:
					return aux, 'esq'
			else:
				return None

			if aux.dir is not None:
				if aux.dir.info == info_apaga:
					return aux, 'dir'
			else:
				return None

		param = {
			'func': achar_antecessor,
			'caminhamento': 'pr',
			'direcao': 'esq'
		}

		no_antecessor = self.percorrer(**param)
		if no_antecessor is not None:
			setattr(no_antecessor[0], no_antecessor[1], None)
			print(f"Elemento '{info_apaga}' removido")
		else:
			raise ValueError(f"Nó '{info_apaga}' não encontrado na árvore '{self.nome}'")

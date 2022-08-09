# Guilherme Azambuja — 149 429

import main

arvore_teste = main.ArvoreBinaria('arvore_teste')
print('-'*80)
arvore_teste.inserir('A')
# Não é necessário passar os parâmetros 'info_antecessor' e 'direcao' ao inserir um primeiro Nó na árvore.
arvore_teste.inserir('B', 'A', 'esq')
arvore_teste.inserir('C', 'A', 'dir')
arvore_teste.inserir('D', 'B', 'esq')
arvore_teste.inserir('E', 'B', 'dir')
arvore_teste.inserir('F', 'C', 'esq')
arvore_teste.inserir('G', 'C', 'dir')
arvore_teste.inserir('H', 'E', 'esq')
arvore_teste.inserir('I', 'E', 'dir')
arvore_teste.inserir('J', 'G', 'esq')
# O objeto 'arvore_teste' é uma árvore encadeada com 4 níveis.
print('-'*80)
arvore_teste.imprimir()
# O método 'imprimir' por padrão utiliza caminhamento pré-fixado à esquerda, porém ambas categorias de caminhamento e
# direção podem ser determinadas utilizando os parâmetros da função. Para caminhamento: 'pr' = pré-fixado,
# 'c' = central, 'po' = pós-fixado. Para direção: 'esq' = para esquerda, 'dir' = para direita.
print()
arvore_teste.imprimir('c', 'dir')
print()
arvore_teste.imprimir('po', 'dir')
print()
print('-'*80)
# arvore_teste.inserir('P', 'M', 'esq')  # Exemplo de erro
# arvore_teste.imprimir('pi', 'dir')     # Exemplo de erro
# Caso parâmetros inválidos sejam passados às funções, erros vão notificar o problema.
arvore_teste.remover('B')
print('-'*80)
arvore_teste.imprimir()
print()
print('-'*80)

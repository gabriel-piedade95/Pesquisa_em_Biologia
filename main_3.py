import inferencia_redes as iR 
import arquivos as arq 

### InferĂȘncia das linhas possiveis para cada gene das marizes funcionais ###

estados = arq.dados_wildtype('estados')

solucoes = iR.resolve_CSP(estados)

iR.imprime_solucoes(solucoes)
import re
import recomendacoes
import mentiras

def responses_handler(message)->str:
    lower_message = message.lower()
    lower_message = lower_message.replace('.', '')

    if lower_message == 'help':
        return 'Esse é o menu de ajuda: \n .conta uma mentira: mentira aleatoria de pedrows; \n .recomendacoes: mostra o status do membro; \n .piada: Eu te conto uma piada muito engraçada (confia);'

    if lower_message == 'ola':
        return 'Olá'

    if lower_message == 'recomendacoes':
        return 'recomendações: \n aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    if lower_message == 'conta uma mentira':
        return mentiras.run_mentira()
    if lower_message == 'piada':
        ...
    if lower_message == '':
        ...
    return 'não tentendi!'
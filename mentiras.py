import random

def run_mentira():
    mentiras = ['eu fui para o aniversario da minha prima e tinha um monte de gente famosa lá.', 'Tem um bar aqui perto de casa que quando eu vou lá beber os caras falam assim "para o som ai galera tá chegando mano pedro"', 'Meu pai te uma desert Eagle em cima do guarda roupas.', 'Eu ganho 2 mil por hora', 'Eu tenho duas faculdades.', 'Eu tenho um servidor em casa pow.', 'O meu pc é foda pow.', 'Eu ganho 5 mil em cada relatorio que eu faço', 'Eu só pego mina assim pow... https://br.pinterest.com/pin/988188343212123386/', 'ontem eu peguei essa daqui oh, https://br.pinterest.com/pin/874050240152063922/', ' Se quiser eu te ensino a pegar mulher.']

    num = random.randrange(0, 11) 
    print(mentiras[num])
    return mentiras[num]

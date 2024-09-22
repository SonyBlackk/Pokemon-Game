import pickle
from pokemon import *
from pessoa import *
import time


def escolher_pokemon_inicial(player):
    print(f'Olá {player}, você poderá escolher agora o Pokemon que ira lhe acompanhar nessa jornada!')

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonFogo('Charmander', level=1)
    squirtle = PokemonAgua('Squirtle', level=1)

    print('Você possui 3 escolhas ')
    print('1 -', pikachu)
    print('2 -', charmander)
    print('3 -', squirtle)

    while True:
        escolha = input('Escolha o seu Pokemon: ')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha invalida')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
    except Exception as erro:
        print('Erro ao salvar o jogo')
        print(erro)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            player = pickle.load(arquivo)
            print('Loading feito com sucesso')
            return player
    except Exception as erro:
        print('Save não encontrado')


if __name__ == '__main__':
    print('------------------------------------------')
    print('Bem vindo ao game Pokemon RPG de terminal!')
    print('------------------------------------------')

    player = carregar_jogo()

    if not player:
        nome = input('Olá, qual o seu nome? ')
        player = Player(nome)
        print(f'Olá {nome}, esse é um mundo habitado por pokemons, '
              f'a partir de agora sua missão é se tornar um mestre dos pokemons')
        print('Capture o maximo de pokemons que conseguir e lute com seus inimigos')
        player.mostrar_dinheiro()

        if player.pokemons:
            print('Já vi que você tem alguns pokemons')
            player.mostrar_pokemons()
        else:
            print('Você não tem nenhum pokemon, portanto precisa escolher um !')
            escolher_pokemon_inicial(player)

        print('Pronto, agora que você ja possui um pokemon, enfrente seu arqui-rival desde o jardim da infância Gary')
        gary = Inimigo(nome='Gary', pokemons=[PokemonAgua('squirtle', level=1)])
        player.batalhar(gary)
        salvar_jogo(player)

    while True:
        print('---------------------------------------')
        print('O que deseja fazer?')
        print('1 - Explorar pelo mundão a fora')
        print('2 - Lutar com um inimigo')
        print('3 - Ver Pokeagenda')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Saindo do jogo')
            time.sleep(2)
            print('Salvando seu game para você :)')
            salvar_jogo(player)
            time.sleep(2)
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemons()
        else:
            print('Escolha invalida')
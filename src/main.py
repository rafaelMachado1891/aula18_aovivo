import time
import random
from controller import pegar_pokemon, adicionar_pokemon

def main():
    while True:
        id = random.randint(1, 350)
        pokemon_schema = pegar_pokemon(id)
        if pokemon_schema:
            print(f'Adicionando {pokemon_schema.name} ao banco de dados')
            adicionar_pokemon(pokemon_schema)
        else: 
            print(f'não foi possivel obter dados para o pokemon id {id}')
        time.sleep(10)

if __name__ == "__main__":
    main()
import random
from enum import IntEnum
from collections import Counter

class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

def assess_game(user_action, computer_action):

    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result


def get_computer_action(lista_acciones_usuario, n):
    if n == 1:
        computer_action = GameAction(0)
    else:
        new_user_action = Counter(lista_acciones_usuario)

        n_rocks = new_user_action[GameAction(0)]
        n_papers = new_user_action[GameAction(1)]
        n_scissors = new_user_action[GameAction(2)]

        if n_rocks == n_papers or n_rocks == n_scissors or n_papers == n_scissors:
            prueba = lista_acciones_usuario[n - 1]
        else:
            prueba = new_user_action[GameAction(2)]
            action_final = max(new_user_action, key=lambda x: new_user_action[x])
            computer_action = Victories[action_final]

    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def main():
    lista_acciones_usuario = []
    victorias_totales = 0

    n_partidas = int(input('Enter the number of games you want to play: '))

    n = 0
    while n < n_partidas:
        try:
            user_action = get_user_action()
            lista_acciones_usuario.append(user_action)
            n += 1  
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action(lista_acciones_usuario, n)
        if assess_game(user_action, computer_action) == GameResult.Victory:
            victorias_totales += 1

    print(f'Wins: {victorias_totales}')

if __name__ == "__main__":
    main()
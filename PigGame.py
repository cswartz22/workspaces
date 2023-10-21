import random


def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)


def computer_turn(game_score, goal):
    turn_score = 0

    while turn_score < goal:
        dice1, dice2 = roll_dice()

        if dice1 == 1 and dice2 == 1:
            game_score = 0
            turn_score = 0
            break
        elif dice1 == 1 or dice2 == 1:
            turn_score = 0
            break
        else:
            turn_score += dice1 + dice2
            print(f"Computer rolled {dice1}, {dice2} Turn total {turn_score}")
    game_score += turn_score
    return game_score


def human_turn(game_score):
    turn_score = 0

    while True:
        dice1, dice2 = roll_dice()
        print(f"You rolled {dice1}, {dice2} Turn total: {turn_score}")
        roll_again = input("Roll again (y/n)? ").lower()

        if roll_again == 'n':
            game_score += turn_score
            break
        elif dice1 == 1 or dice2 == 1:
            break
        else:
            turn_score += dice1 + dice2
    return game_score


def computer_solo(goal):
    total_turns = 0
    score_game = 0

    while score_game < 100 and total_turns < 100:
        score_game = computer_turn(score_game, goal)
        total_turns += 1
        print(f'Turns: {total_turns} Score: {score_game}')
    print(f'Turns: {total_turns}')
    return total_turns


def world_championship(games, goal_1, goal_2):
    player1_w = 0
    player2_w = 0

    for game in range(games):
        player1_score = computer_solo(goal_1)
        player2_score = computer_solo(goal_2)

        if player1_score > player2_score:
            player1_w += 1
        elif player2_score > player1_score:
            player2_w += 1

        print(f'Player 1: {player1_score} Player 2: {player2_score}')
        print(f'Player 1 Wins: {player1_w} Player 2 Wins: {player2_w}')


def human_vs_computer():
    human_score = 0
    computer_score = 0

    while human_score < 100 and computer_score < 100:
        human_score = human_turn(human_score)
        print(f'You: {human_score} Computer: {computer_score}')

        if human_score >= 100:
            print("Congratulations!")
            break

        computer_score = computer_turn(computer_score, 20)
        print(f'You: {human_score} Computer: {computer_score}')

        if computer_score >= 100:
            print("Congrats! You stink!")


if __name__ == '__main__':
    world_championship(7, 30, 25)
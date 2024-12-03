import game
import time


game.initPlayers()
time.sleep(2)
player1 = game.createNewPlayer('Handoko', damage=15, defensePower=5)
player2 = game.createNewPlayer('Susi', damage=10, defensePower=3)
player3 = game.createNewPlayer('Lee', damage=20, defensePower=8)

game.addPlayer(player1)
print(f'{player1['name']} memasuki permainan | damage: {player1['damage']} | defense: {player1['defensePower']}')
time.sleep(2)
game.addPlayer(player2)
print(f'{player2['name']} memasuki permainan | damage: {player2['damage']} | defense: {player2['defensePower']}')
time.sleep(2)
game.addPlayer(player3)
print(f'{player3['name']} memasuki permainan | damage: {player3['damage']} | defense: {player3['defensePower']}')
time.sleep(3)

print()
print('GAME START APT APT\n')
time.sleep(2)

# handoko mukul susi
print('Handoko menyerang Susi!')
time.sleep(1)
game.attackPlayer(player1, player2)
print(f'Health Susi: {player2['health']}, Skor Handoko: {player1['score']}\n')
time.sleep(2)

# lee defense
print('Lee mode bertahan.\n')
time.sleep(1)
game.setPlayer(player3, 'defense', True)
time.sleep(2)

# susi mukul lee
print('Susi menyerang Lee!')
time.sleep(1)
game.attackPlayer(player2, player3)
print(f'Health Lee: {player3['health']}, Skor Susi: {player2['score']}\n')
time.sleep(2)

# lee mukul handoko
print('Lee menyerang Handoko!')
time.sleep(1)
game.attackPlayer(player3, player1)
print(f'Health Handoko: {player1['health']}, Skor Lee: {player3['score']}\n')
time.sleep(2)

# lee mukul susi
print('Lee menyerang Susi!')
time.sleep(1)
game.attackPlayer(player3, player2)
print(f'Health Handoko: {player2['health']}, Skor Lee: {player3['score']}\n')
time.sleep(2)

# handoko mukul susi
print('Handoko menyerang Susi!')
time.sleep(1)
game.attackPlayer(player1, player2)
print(f'Health Susi: {player2['health']}, Skor Handoko: {player1['score']}\n')
time.sleep(2)

# lee mukul susi
print('Lee menyerang Susi!')
time.sleep(1)
game.attackPlayer(player3, player2)
print(f'Health Handoko: {player2['health']}, Skor Lee: {player3['score']}\n')
time.sleep(2)

# handoko mukul susi
print('Handoko menyerang Susi!')
time.sleep(1)
game.attackPlayer(player1, player2)
print(f'Health Susi: {player2['health']}, Skor Handoko: {player1['score']}\n')
time.sleep(2)

time.sleep(3)
game.removePlayer('Susi')

# lee defense
print('Lee mode bertahan.\n')
time.sleep(1)
game.setPlayer(player3, 'defense', True)
time.sleep(2)

# lee mukul handoko
print('Lee menyerang Handoko!')
time.sleep(1)
game.attackPlayer(player3, player1)
print(f'Health Handoko: {player1['health']}, Skor Lee: {player3['score']}\n')
time.sleep(2)

# handoko defense
print('Handoko mode bertahan.\n')
time.sleep(1)
game.setPlayer(player1, 'defense', True)
time.sleep(2)

# handoko mukul lee
print('Handoko menyerang Lee!')
time.sleep(1)
game.attackPlayer(player1, player3)
print(f'Health Handoko: {player3['health']}, Skor Lee: {player1['score']}\n')
time.sleep(2)

print('Lee Menyerah!\n')
time.sleep(3)
print('Game Over\n')
time.sleep(5)
game.displayMatchResult()



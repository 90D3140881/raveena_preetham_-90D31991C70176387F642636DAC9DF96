class Player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(Player):
  def play(self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is batting.")

batsman = Batsman()
bowler = Bowler()

batsman.play()
bowler.play()
    
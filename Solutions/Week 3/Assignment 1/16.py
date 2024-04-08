def rps(p1, p2):
    if p1 == p2:
        return "It's a draw"
    elif p1 == "Rock" and p2 == "Scissors":
        return "The winner is p1"
    elif p1 == "Scissors" and p2 == "Paper":
        return "The winner is p1"
    elif p1 == "Paper" and p2 == "Rock":
        return "The winner is p1"
    else:
        return "The winner is p2"

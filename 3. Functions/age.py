# def vote(age: int) -> str:
#     if age < 18:
#         return "You cannot vote"
#     return "You can vote"


def vote(age: int) -> None:
    if age < 18:
        print("You cannot vote")
        return
    print("You can vote")


# ans = vote(90)
# print(ans)
vote(55)

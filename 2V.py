import random

class Chef:
    def __init__(self, name, skill, speed, creativity):
        self.name = name
        self.skill = skill
        self.speed = speed
        self.creativity = creativity
        self.score = 0
        self.active = True

    def compete(self, opponent):
        points = self.skill + self.creativity - opponent.speed
        if points < 1:
            points = 1

        self.score += points
        print(f"{self.name} earns {points} points. Score: {self.score}")
        opponent.take_points(points)

    def take_points(self, points):
        self.score -= points
        if self.score < 0:
            self.score = 0
            self.active = False
            print(f"{self.name} has been eliminated!")

    def is_active(self):
        return self.active

    def show_stats(self):
        print(
            f"Name: {self.name}, "
            f"Skill: {self.skill}, "
            f"Speed: {self.speed}, "
            f"Creativity: {self.creativity}, "
            f"Score: {self.score}, "
            f"Active: {self.active}"
        )

class CookingContest:
    def __init__(self):
        self.chefs = []

    def add_chef(self, chef):
        self.chefs.append(chef)

    def get_active_chefs(self):
        return [chef for chef in self.chefs if chef.is_active()]

    def start_contest(self):
        print("Contest started!\n")

        while len(self.get_active_chefs()) > 1:
            active_chefs = self.get_active_chefs()
            chef1, chef2 = random.sample(active_chefs, 2)

            print(f"{chef1.name} competes with {chef2.name}")
            chef1.compete(chef2)

            if chef2.is_active():
                print(f"{chef2.name} competes with {chef1.name}")
                chef2.compete(chef1)

            print("\nCurrent stats:")
            for chef in self.chefs:
                chef.show_stats()
            print("-" * 40)

    def show_winner(self):
        winner = self.get_active_chefs()[0]
        print(f"\nWinner: {winner.name}")


chef1 = Chef("Aktoty", skill=10, speed=5, creativity=7)
chef2 = Chef("Asylai", skill=9, speed=6, creativity=6)
chef3 = Chef("Aisha", skill=8, speed=4, creativity=8)

contest = CookingContest()
contest.add_chef(chef1)
contest.add_chef(chef2)
contest.add_chef(chef3)

contest.start_contest()
contest.show_winner()
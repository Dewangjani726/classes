class Animals:
    lion = "simba"
    monkey = "abu"
    # elephant = "raju"
    # tiger = "bagira"

    def run():
        print("Most animals can run.")

    def swim():
        print("All animals can't swim.")

    def roar():
        print("All mammals can roar.")

class mammals(Animals):
    lion = "bagga"
    monkey = "chimpu"

    def run():
        print("Most mammals can run.")

    def roar():
        print("No mammals can roar.")

maml1 = mammals.swim()
ani1 = mammals.roar()

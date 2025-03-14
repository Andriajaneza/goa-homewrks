def all(HP):
    HP = (all(1))
    def increes_health(a):
        a = 1
        HP += a
    def decrees_health(b):
        a = -1
        HP += a
    def Main():
        increes_health()
        decrees_health()
        return HP
    Main()
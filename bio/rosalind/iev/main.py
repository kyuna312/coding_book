def calculate_offspring(l):
    offspring = (1*l[0] + 1*l[1] + 1*l[2] + 0.75*l[3] + 0.5*l[4] + 0*l[5]) * 2
    return offspring 

if __name__ == "__main__":
    with open("./rosalind_iev.txt", "r") as f:
        l = [float(i) for i in f.readline().strip().split(" ")]
    print(calculate_offspring(l))

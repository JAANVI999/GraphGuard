import sys
import numpy

def read_ground_truth(network_name):
    with open(f"../data/{network_name}_gt.csv", "r") as f:
        goodusers, badusers = set(), set()
        for line in f:
            user, label = line.strip().split(",")
            if label == "-1":
                badusers.add(user)
            else:
                goodusers.add(user)
    return goodusers, badusers


def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)


def process_file(fname, goodusers, badusers):
    NLINES = count_lines(fname)
    Ys, Ys2, X = [], [], []
    for NUSERS in range(1, 250):
        c11, c12, c21, c22 = 0, 0, 0, 0
        with open(fname, "r") as f:
            for i, line in enumerate(f):
                user, _, _ = line.strip().split(",")
                if i < NUSERS:
                    if user in goodusers:
                        c11 += 1
                    elif user in badusers:
                        c12 += 1
                elif i >= NLINES - NUSERS:
                    if user in goodusers:
                        c21 += 1
                    elif user in badusers:
                        c22 += 1
        X.append(c21 + c22 + 1)
        Ys.append((c22 + 0.001) / (c21 + c22 + 0.001))
        Ys2.append((c11 + 0.001) / (c11 + c12 + 0.001))
    fww.write("%f, %f\n" % (float(numpy.mean(Ys)), float(numpy.mean(Ys2))))
    fww.close()


import math


def num_atoms(weight, atomic_weight=196.67):

    avogadro_constant = 6.022*math.pow(10, 23)
    moles = weight/atomic_weight
    atoms = moles*avogadro_constant
    print(atoms)
    return moles, atoms


num_atoms(10)

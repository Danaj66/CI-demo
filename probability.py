from itertools import product

BASE_DEFENSE = 5000


def can_attack_hit(attack, counters):
    return attack > BASE_DEFENSE + counters


def calculate_probability(attacks, counter_type):
    total = len(attacks)
    successful = 0

    for attack in attacks:
        if can_attack_hit(attack, counter_type):
            successful += 1

    return round(successful / total * 100, 2)


def distribute_dons(base_attacks, dons=10):
    results = []

    allocations = product(range(dons + 1), repeat=len(base_attacks))

    for allocation in allocations:
        if sum(allocation) == dons:
            boosted = [
                atk + (don * 1000)
                for atk, don in zip(base_attacks, allocation)
            ]
            results.append(boosted)

    return results

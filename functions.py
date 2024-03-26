
import math

def count_values(data, attribute_index):
    values_count = {}
    for row in data:
        value = row[attribute_index]
        if value not in values_count:
            values_count[value] = 1
        else:
            values_count[value] += 1
    return values_count, len(values_count)

def count_attribute_decision_values(data, attribute_index, decision_index, possible_values):
    values_count = {key: {decision: 0 for decision in possible_values} for key in set(row[attribute_index] for row in data)}
    for row in data:
        attribute_value = row[attribute_index]
        decision_value = row[decision_index]
        values_count[attribute_value][decision_value] += 1
    return values_count

def count_entropy(decision_class):
    total_count = sum(decision_class.values())
    entropy = 0
    for count in decision_class.values():
        probability = count / total_count
        if probability > 0:
            entropy -= probability * math.log2(probability)
        else:
            entropy = 0
    return entropy

def count_entropy_for_attribute(attribute_values_counts, decision_values):
    entropies = {}
    for value, counts in attribute_values_counts.items():
        entropy = 0
        total_count = sum(counts.values())
        if total_count > 0:
            probabilities = [counts[decision] / total_count for decision in decision_values]
            for probability in probabilities:
                if probability > 0:
                    entropy -= probability * math.log2(probability)
        entropies[value] = entropy
    return entropies

def atribute_info(data, attribute_count, attribute_index, decision_values, decision_index):
    decision_value_count_for_attribute = count_attribute_decision_values(data, attribute_index, decision_index, decision_values)
    entropies = count_entropy_for_attribute(decision_value_count_for_attribute, decision_values)
    info = 0
    for value in attribute_count:
        info += (attribute_count.get(value) / sum(attribute_count.values())) * entropies.get(value)
    return info

def gain(entropy_info, attribute_info):
    return entropy_info - attribute_info

def gain_ratio(data, attribute_values, decision_attribute_values_count, attribute_index, decision_attribute_index):
    decision_attribute_entropy = count_entropy(decision_attribute_values_count)
    attribute_info = atribute_info(data, attribute_values, attribute_index, decision_attribute_values_count, decision_attribute_index)
    gain_value = gain(decision_attribute_entropy, attribute_info)
    split_info = count_entropy(attribute_values)
    gain_ratio = gain_value / split_info
    return gain_ratio

def get_best_split(data, attributes, decision_attribute_index):
    decision_values, _ = count_values(data, decision_attribute_index)
    best_attribute_index = None 
    best_gain_ratio = -float('inf')
    for attribute_index in attributes:
        if attribute_index != decision_attribute_index:
            attribute_values, _ = count_values(data, attribute_index)
            current_gain_ratio = gain_ratio(data, attribute_values, decision_values, attribute_index, decision_attribute_index)
            if current_gain_ratio > best_gain_ratio:
                best_gain_ratio = current_gain_ratio
                best_attribute_index = attribute_index
    return best_attribute_index

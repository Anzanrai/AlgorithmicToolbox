# Uses python3


def get_optimal_value(capacity, sorted_data_):
    value = 0.
    counter = 0
    while capacity and counter in range(len(sorted_data_)):
        if sorted_data_[counter].get('weight') <= capacity:
            value += sorted_data_[counter].get('value')
            capacity -= sorted_data_[counter].get('weight')
        else:
            value += sorted_data_[counter].get('value_per_kilo')* capacity
            capacity -= capacity
        counter += 1
    # write your code here

    return value


if __name__ == "__main__":
    data = list(map(int, input().split()))
    n, capacity = data[0:2]
    data_ = []
    for i in range(n):
        values, weights = list(map(int, input().split()))
        data_.append({'value': values, 'weight': weights, 'value_per_kilo': values/weights})
    sorted_data_ = sorted(data_, key=lambda k: k['value_per_kilo'], reverse=True)
    opt_value = get_optimal_value(capacity, sorted_data_)
    print("{:.10f}".format(opt_value))

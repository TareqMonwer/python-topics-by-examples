def decimal_to_binary(decimal, result):
    if decimal == 0:
        return result

    result = f'{decimal % 2}{result}'
    return decimal_to_binary(decimal // 2, result)


if __name__ == "__main__":
    print(decimal_to_binary(233, ""))

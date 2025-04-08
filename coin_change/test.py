def make_change(coins, amount = int(input("Choose an Amount: "))):
    """
    Calculates the minimum number of coins needed to make change for a given amount.

    Args:
        amount (int): The amount to make change for.
        coins (list): A list of coin denominations.

    Returns:
        dict: A dictionary containing the count of each coin denomination,
              or None if it's not possible to make change.
    """
    coins.sort(reverse=True)  # Sort coins in descending order
    change = {}
    remaining_amount = amount

    for coin in coins:
        while remaining_amount >= coin:
            remaining_amount -= coin
            change[coin] = change.get(coin, 0) + 1

    if remaining_amount == 0:
        return change
    else:
        return None

# Example usage:

result = make_change([1, 5, 10, 25, 50, 100, 500])
if result:
    print(f"Change for {amount} cents:")
    for coin, count in result.items():
        print(f"{count} x {coin} {'cent' if count == 1 else 'cents'}")
else:
    print(f"Cannot make change for {amount} cents with the given coins.")



make_change([1, 5, 10, 25, 50, 100, 500])
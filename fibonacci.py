def fibonacci(n):
    """Return a list of the first n Fibonacci numbers."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def main():
    n = int(input("Enter the number of terms: "))
    print("Fibonacci Series:")
    print(" ".join(str(x) for x in fibonacci(n)))


if __name__ == "__main__":
    main()

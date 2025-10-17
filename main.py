def main():
    user_input = input()
    try:
        num = int(user_input)
        print(num * num)
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    main()
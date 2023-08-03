def main():
    # Initialize an empty list to store the sales for each day of the week
    sales_list = []

    # Prompt the user to enter the sales for each day of the week
    for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
        sales = float(input(f"Enter sales for {day}: "))
        sales_list.append(sales)

    # Calculate the total sales for the week using a loop
    total_sales = 0
    for sales in sales_list:
        total_sales += sales

    # Display the total sales for the week
    print("Total sales for the week:", total_sales)

if __name__ == "__main__":
    main()

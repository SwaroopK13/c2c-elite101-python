
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""



def frequentlyaskedquestions() :
    questions = input("Here are some frequently offered questions. Enter an input based on what question you need answering. Enter 1 if you would like to know when the company was started. Enter 2 if you would like to know the owner of the store. Enter 3 if you would like to know the return policy we offer!")
    if questions == "1" :
        print("The company was started on the owners birthday of October 13th of 2025. he owner decided to start the store because he believed the world was in need of bedroom essentials like towels and bedsheets, but he also realized there was a lack of buckets, so he decided to build a store that did just that. ")
    elif questions == "2" :
        print("The Owner of the store is Swaroop Kadiyam, who is a sophmore at Indepence High School in Frisco, Texas.")
    elif questions == "3" :
        print("Customers are able to return any UNOPENED goods within 3 weeks of purchase, or OPENED goods as long as there is a manufacturing error such as a dent or scratch on the product. Recipt is also needed in order to process the return. ")
    else :
        ("I unfortunately, cannot understand that. Please re-enter an INTEGER of your choice.")
    user_name()

def storehoursandlocation() :
    print("Bed, Buckets, and Beyond is located on 123 Main Street in Frisco Texas. Our store timings are 9-5 on Weekdays and 8-3 on Weekends.")
    user_name()

def catalog_and_prices() :
    prices = input("Which of the following items would you like to see the prices for? Type 1 for the price for a bucket, 2 for the price of a blanket, 3 for the price of a bar of soap, type 4 for the price of a towel, and type 5 for the price of a bottle of scented handsanitizer.")
    if prices == "1" :
        print("The price for a large 7 gallon bucket is $29.99.")
    elif prices == "2" :
        print("The price for a queen blanket is $45.97. ")
    elif prices == "3" :
        print("The price for a bar of soap is $4.99")
    elif prices == "4" :
        print("The price for a 16 by 28 inch towel is $10.99. ")
    elif prices == "5" :
        print("The price for a bottle of scented handsanitizer is $2.99.")
    else :
        print("Unfortunately, I could not understand that. Please make sure to only input an integer of the option you would like.")
    user_name()

def user_name():
    name =  input("Hello! Welcome to Bed, Buckets and Beyond! May I have your name?  : ")
    print(f"Hello {name}! Nice to meet you!")
    userinput = input("If you want to see frequently asked questions, Press 1. If you want information about store hours and the location, please press 2. If you want to see the products we offer as well as the prices, press 3! If you want to end the conversation, please enter 4.    : ").lower()
    if userinput == "1" :
        frequentlyaskedquestions()
    elif userinput == "2" :
        storehoursandlocation()
    elif userinput == "3" :
        catalog_and_prices()
    elif userinput == "4" :
        print("Thank you for your time today at Bed, Buckets and Beyond! Enjoy your day!")
    else :
        print("I'm not quite sure I understand that, please make sure to only input a number!")
        user_name()
user_name()

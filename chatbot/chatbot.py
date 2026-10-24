# Load agriculture knowledge
def load_knowledge():

    with open("data/agriculture_knowledge.txt", "r", encoding="utf-8") as file:
        knowledge = file.read()

    return knowledge


# Agriculture chatbot
def agriculture_chatbot(question):

    knowledge = load_knowledge()

    question = question.lower()

    if "rice" in question:
        return "Here is information about rice:\n\n" + knowledge.split("TOMATO")[0]

    elif "tomato" in question:
        tomato_info = knowledge.split("TOMATO")[1].split("WHEAT")[0]
        return "Here is information about tomato:\n\n" + tomato_info

    elif "wheat" in question:
        wheat_info = knowledge.split("WHEAT")[1].split("FERTILIZER")[0]
        return "Here is information about wheat:\n\n" + wheat_info

    elif "fertilizer" in question:
        fertilizer_info = knowledge.split("FERTILIZER")[1].split("IRRIGATION")[0]
        return "Here is fertilizer information:\n\n" + fertilizer_info

    elif "irrigation" in question:
        irrigation_info = knowledge.split("IRRIGATION")[1].split("PLANT DISEASES")[0]
        return "Here is irrigation information:\n\n" + irrigation_info

    elif "disease" in question:
        disease_info = knowledge.split("PLANT DISEASES")[1]
        return "Here is plant disease information:\n\n" + disease_info

    else:
        return "I can help you with rice, tomato, wheat, fertilizer, irrigation and plant diseases."


# Start chatbot
while True:

    question = input("Farmer: ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    answer = agriculture_chatbot(question)

    print("\nAI Agriculture Assistant:")
    print(answer)
import json
import random

# Get recent message
def get_recent_message():

    # Define the file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system", 
        "content": "You are interviewing the user for a job as a retail assistant. Ask short questions that relevant to the junior position. Your name is Rachel. The user is called Shaun. Keep your answers to under 30 words. "
    }


    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Yours response will include some dry humour."
    else: 
        learn_instruction["content"] = learn_instruction["content"] + " Yours response will include rather challenging question."


    # Append instruction to message
    messages.append(learn_instruction)


    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file) 

            # Append the last 5 items data
            if data:
                if len(data) < 5: 
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5]:
                        messages.append(item)        
    except Exception as e:  
        print(e)
        pass

    # Return msg
    return messages         
   
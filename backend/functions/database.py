import json
import random

# Get recent message
def get_recent_message():

    # Define the file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system", 
        "content": "You are a interviewer for tech position in programming language.Your name is rachel. ask me in which language i want the interview perpetration. Keep responses under 30 words. "
    }
 

    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0,1)
    if x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + " Yours response will include some dry humour."
    else: 
        learn_instruction["content"] = learn_instruction["content"] + " Your response will include asking me wired question also."


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
                    for item in data[-5:]:
                        messages.append(item)        
    except Exception as e:  
        print(e)
        pass

    # Return msg
    return messages   


 # Store Messages
def store_messages(request_message, response_message):

    # Define the file name
    file_name = "stored_data.json"

    # Get recent message
    messages = get_recent_message()[1:]

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


    # Reset messages
def reset_messages():

        # Overwrite current file with nothing
        open("stored_data.json", "w")    




    
   
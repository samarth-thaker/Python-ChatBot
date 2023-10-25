import re
import longresponses as long

def checkAllMessages(message):
    highestProbList = {}
    def response(botResponse, listOfWords, singleResponse = False, requiredWords = []):
        nonlocal highestProbList
        highestProbList[botResponse] = message_probability(message, listOfWords, singleResponse, requiredWords)
      
      #Response--------------------------------------------------------------------
      
      
      
    response('I\'m doing well and you?',  ['how', 'are', 'you', 'doing'], requiredWords=['how'])
    response('Thank you!', ['you', 'are', 'amazing'], requiredWords=['amazing'])
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], singleResponse=True)
    response(long.R_Eating, ['what', 'you', 'eat'],requiredWords=['you', 'eat'])
    bestMatch = max(highestProbList, key = highestProbList.get)
    #print(highestProbList)
    return long.unknown() if highestProbList[bestMatch]<1 else bestMatch
        
    
def message_probability(userMessage, recognisedWords, singleResponse=False, requiredWords=[]):
    message_certainty = 0
    has_required_words = True

    
    for word in userMessage:
        if word in recognisedWords:
            message_certainty += 1

    
    percentage = float(message_certainty) / float(len(recognisedWords))
    for word in requiredWords:
        if word not in userMessage:
            has_required_words  = False
            break
    if has_required_words or singleResponse:
        return int(percentage*100)
    else:
        return 0
    
        
      
        



def get_response(user_input):
    splitMessage = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = checkAllMessages(splitMessage)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
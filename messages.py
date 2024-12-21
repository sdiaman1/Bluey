from enum import Enum
import random

class MessageType(Enum):
  REQUEST = 1
  RESPONSE = 2

# The messages dictionary; key = request, value = array of responses.
messages = {}

def ReadFromFile(name):
  """
  Reads the messages from the specified file.

  :param name: the name of the file.
  """
  with open(name, "r") as file:
    request = ""
    response = ""

    for line in file:
      line = line.strip()
      # Comments start with ";".
      index = line.find(";")
      if index >= 0:
        line = line[:index]

      if line:
        # Get the type of message; request ("Written") or response ("Read").
        if line.startswith("["):
          if "Written" in line:
            messageType = MessageType.REQUEST
            # If there's a previous request and response then save them in the messages dictionary.
            Add(request, response)
            request = ""
          elif "Read" in line:
            messageType = MessageType.RESPONSE
            response = ""
        else:
            # Append the HEX string (before the "  ") to the request or response.
            end = line.find("  ")
            if end >= 0:
              line = line[:end]
            line = line.replace(" ", "")

            if messageType == MessageType.REQUEST:
                request += line
            elif messageType == MessageType.RESPONSE:
                response += line

    Add(request, response)

def Add(request, response):
  """
  Adds the specified request and response to the messages dictionary.
  """
  if request and response:
    value = messages.get(request)
    if value is None:
      # Key does not exist in the dictionary, add it.
      value = []
    value.append(response)
    messages[request] = value

def GetRandomResponse(request):
  """
  Returns a random response from the messages dictionary for the specified request.
  """
  value = messages.get(request)
  if value is None:
    return None
  else:
    index = random.randint(0, len(value) - 1)
    return value[index]

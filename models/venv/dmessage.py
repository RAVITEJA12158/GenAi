from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
load_dotenv()
chat_template = ChatPromptTemplate.from_messages(
    [ 
        ('system', "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ('human', "{input}" )
      ])
history = []
chat_prompt=chat_template.invoke({'history': history, 'input': "Hello, how are you?"})
history.append(chat_prompt.messages[1])      


from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
template=PromptTemplate(
    template="""
You are a helpful assistant that translates {input_language} to {output_language}.""",
    input_variables=["input_language", "output_language"],
    validate_template=True
)
# template.save("template.json")


from langchain_core.load import dumps

template_json = dumps(template)

with open("template.json", "w") as f:
    f.write(template_json)
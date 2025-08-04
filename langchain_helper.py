from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.llms import HuggingFacePipeline

# Global chain instance to avoid reloading
_chain = None

def get_chain():
    global _chain
    if _chain is not None:
        return _chain

    model_id = "distilgpt2"  # Lightweight model for CPU use

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id).to("cpu")

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=30)
    llm = HuggingFacePipeline(pipeline=pipe)

    prompt = PromptTemplate(
        input_variables=["cuisine", "theme", "location"],
        template="""
Suggest a unique, creative restaurant name for the following details:

Cuisine: {cuisine}
Theme: {theme}
Location: {location}

Restaurant Name:
"""
    )

    _chain = LLMChain(prompt=prompt, llm=llm)
    return _chain

def generate_restaurant_name_and_items(cuisine, theme="Modern Fusion", location="Delhi"):
    chain = get_chain()
    name = chain.run({
        "cuisine": cuisine,
        "theme": theme,
        "location": location
    }).strip()

    menu_map = {
        "Indian": "Samosa, Paneer Tikka, Butter Naan",
        "Italian": "Margherita Pizza, Pasta Alfredo, Tiramisu",
        "Japanese": "Sushi, Ramen, Tempura",
        "Mexican": "Tacos, Burritos, Quesadillas",
        "Chinese": "Dumplings, Kung Pao Chicken, Spring Rolls",
        "Thai": "Green Curry, Pad Thai, Mango Sticky Rice",
        "French": "Croissant, Coq au Vin, Crème Brûlée",
        "Greek": "Gyros, Moussaka, Baklava",
        "Spanish": "Paella, Tapas, Churros",
        "Moroccan": "Tagine, Couscous, Harira",
        "Turkish": "Kebabs, Meze, Baklava",
        "Vietnamese": "Pho, Banh Mi, Spring Rolls",
        "Lebanese": "Hummus, Shawarma, Fattoush",
        "Korean": "Bibimbap, Kimchi, Bulgogi",
        "Ethiopian": "Injera, Doro Wat, Kitfo"
    }

    items = menu_map.get(cuisine, "Chef Special 1, Chef Special 2")

    return {
        "restaurant_name": name,
        "menu_items": items
    }

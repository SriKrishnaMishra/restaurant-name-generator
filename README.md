# 🍽️ Restaurant Name Generator

An AI-powered web app that generates creative restaurant names and menu ideas based on your selected cuisine. Whether you're a food entrepreneur, hobbyist, or just having fun, this tool helps spark culinary branding inspiration in seconds!

## 🚀 Features

- **Creative Name Generation**: Get unique, fancy restaurant names tailored to your chosen cuisine.
- **Menu Suggestions**: AI-curated menu items that match the restaurant's theme.
- **Interactive UI**: Built with Streamlit for a smooth and intuitive user experience.
- **Custom Cuisine Input**: Don’t see your favorite cuisine? Just type it in!
- **Modern Styling**: Clean layout with colorful visuals for an engaging experience.

## 🛠️ Tech Stack

- [LangChain](https://www.langchain.com/) – for chaining LLM prompts and outputs
- [OpenAI](https://openai.com/) – for generating creative content
- [Streamlit](https://streamlit.io/) – for building the interactive web app
- `dotenv` – for secure API key management

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/SriKrishnaMishra/restaurant-name-generator.git
   cd restaurant-name-generator

   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

streamlit run main.py

 Project Structure
- main.py – Streamlit app logic and UI
- langchain_helper.py – LangChain chains and prompt templates
- requirements.txt – Python dependencies
- .env.example – Sample environment file for API key setup
🧠 How It Works
- You select or enter a cuisine.
- The app uses LangChain's SequentialChain to:
- Generate a restaurant name using OpenAI.
- Generate a themed menu based on that name.
- Results are displayed instantly in the app.
💡 Inspiration
This project blends creativity with AI to help users brainstorm restaurant concepts. Perfect for branding exercises, pitch decks, or just having fun with food ideas!
📜 License
This project is licensed under the MIT License.


Let me know if you'd like to add a demo link, screenshots, or contributor credits. I can also help you write a short project description for your GitHub profile or portfolio!



Let me know if you'd like to add a demo link, screenshots, or contributor credits. I can also help you write a short project description for your GitHub profile or portfolio!

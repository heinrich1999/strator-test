# AI Automation Developer Test Task – Strator

This project runs an automation agent that:

- Utilizes OpenAI to generate a summary of AI trends
- Creates a Notion page with the content
- Sends it to a Zapier webhook to replicate integration

## How I Ran the Test

1. Cloned the repo using Git Bash (original repo):

   ```bash
   git clone https://github.com/NinaTre-alt/strator-test.git
   cd strator-test

   ```

2. Copied the example environment file and added API keys.
   First, I copied the `.env.example` file to a new `.env` file using Git Bash:

   ```bash
   cp .env.example .env

   ```

3. Then I opened the `.env` file using VS Code and added the API keys provided:

   ```env
   OPENAI_API_KEY=...
   NOTION_TOKEN=...
   NOTION_DATABASE_ID=...
   ZAPIER_WEBHOOK_URL=...
   RUNPOD_API_KEY=...

   ```

4. Created and activated a virtual environment using Git Bash:

   ```bash
   python -m venv venv
   source venv/Scripts/activate

   ```

5. Installed all required Python packages using `requirements.txt`:

   ```bash
   pip install -r requirements.txt

   ```

6. Ran the test script to execute the full automation flow:

   ```bash
   python run_test_agent.py
   ```

7. ## Test Status

   - ✅ OpenAI integration: Successful
   - ✅ Notion page created
   - ✅ Zapier webhook triggered (Response code: 200)

   All services were connected and functioned as expected.

## Output

```text
    AI Summary:
     Here are three emerging AI trends:

    1. **Generative AI Advancements**: The rise of generative AI tools, such as those used for text, image, and video creation, is transforming content creation across various industries. Models like OpenAI's GPT and DALL-E, as well as tools for deepfake technology, are becoming more sophisticated, enabling new forms of creativity and personalization in marketing, entertainment, and design.

    2. **AI for Sustainability**: There is a growing focus on leveraging AI to address environmental challenges. AI technologies are increasingly being used for monitoring climate change, optimizing energy consumption, and enhancing resource management in agriculture and water systems. This trend reflects a broader commitment to integrating AI solutions with sustainability goals.

    3. **Explainable AI (XAI)**: As AI systems become more prevalent, there's an increasing demand for transparency and interpretability in AI decision-making processes. Explainable AI aims to create models that can provide human-understandable justifications for their outputs, which is essential for building trust and ensuring compliance with regulations in sectors like finance, healthcare, and legal systems.

    Notion page created: https://www.notion.so/Trend-Report-1ea7b8c603438173802ee6809a61448f
    Zapier response code: 200

```

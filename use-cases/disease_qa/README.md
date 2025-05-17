# Disease Information App

An interactive browser-based application that provides structured information about diseases using Perplexity's Sonar API. This app generates a standalone HTML interface that allows users to ask questions about various diseases and receive organized responses with citations.

![Disease Information App Screenshot](https://via.placeholder.com/800x450.png?text=Disease+Information+App)

## 🌟 Features

- **User-Friendly Interface**: Clean, responsive design that works across devices
- **AI-Powered Responses**: Leverages Perplexity's Sonar API for accurate medical information
- **Structured Knowledge Cards**: Organizes information into Overview, Causes, and Treatments
- **Citation Tracking**: Lists sources of information with clickable links
- **Client-Side Caching**: Prevents duplicate API calls for previously asked questions
- **Standalone Deployment**: Generate a single HTML file that can be used without a server
- **Comprehensive Error Handling**: User-friendly error messages and robust error management

## 📋 Requirements

- Python 3.6+
- Jupyter Notebook or JupyterLab (for development/generation)
- Required packages:
  - requests
  - pandas
  - python-dotenv
  - IPython

## 🚀 Setup & Installation

1. Clone this repository or download the notebook
2. Install the required packages:

```bash
pip install requests pandas python-dotenv ipython
```

3. Set up your Perplexity API key:
   - Create a `.env` file in the same directory as the notebook
   - Add your API key: `PERPLEXITY_API_KEY=your_api_key_here`

## 🔧 Usage

### Running the Notebook

1. Open the notebook in Jupyter:

```bash
jupyter notebook Disease_Information_App.ipynb
```

2. Run all cells to generate and launch the browser-based application
3. The app will automatically open in your default web browser

### Using the Generated HTML

You can also directly use the generated `disease_qa.html` file:

1. Open it in any modern web browser
2. Enter a question about a disease (e.g., "What is diabetes?", "Tell me about Alzheimer's disease")
3. Click "Ask" to get structured information about the disease

### Deploying the App

For personal or educational use, simply share the generated HTML file.

For production use, consider:
1. Setting up a proper backend to secure your API key
2. Hosting the file on a web server
3. Adding analytics and user management as needed

## 🔍 How It Works

This application:

1. Uses a carefully crafted prompt to instruct the AI to output structured JSON
2. Processes this JSON to extract Overview, Causes, Treatments, and Citations
3. Presents the information in a clean knowledge card format
4. Implements client-side API calls with proper error handling
5. Provides a responsive design suitable for both desktop and mobile

## ⚙️ Technical Details

### API Structure

The app expects the AI to return a JSON object with this structure:

```json
{
  "overview": "A brief description of the disease.",
  "causes": "The causes of the disease.",
  "treatments": "Possible treatments for the disease.",
  "citations": ["https://example.com/citation1", "https://example.com/citation2"]
}
```

### Files Generated

- `disease_qa.html` - The standalone application
- `disease_app.log` - Detailed application logs (when running the notebook)

### Customization Options

You can modify:
- The HTML/CSS styling in the `create_html_ui` function
- The AI model used (default is "sonar-pro")
- The structure of the prompt for different information fields
- Output file location and naming

## 🛠️ Extending the App

Potential extensions:
- Add a Flask/Django backend to secure the API key
- Implement user accounts and saved questions
- Add visualization of disease statistics
- Create a comparison view for multiple diseases
- Add natural language question reformatting
- Implement feedback mechanisms for answer quality

## ⚠️ Important Notes

- **API Key Security**: The current implementation embeds your API key in the HTML file. This is suitable for personal use but not for public deployment.
- **Not Medical Advice**: This app provides general information and should not be used for medical decisions. Always consult healthcare professionals for medical advice.
- **API Usage**: Be aware of Perplexity API rate limits and pricing for your account.

## 📜 License

[MIT License](LICENSE)

## 🙏 Acknowledgements

- This project uses the [Perplexity AI Sonar API](https://docs.perplexity.ai/)
- Inspired by interactive knowledge bases and medical information platforms

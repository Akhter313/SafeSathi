# SafeSathi 🛡️

**AI-driven WhatsApp-based Interface for Social Engineering Awareness & Scam Detection**

SafeSathi is designed to help users (especially in rural/semi-urban India) detect online scams, check suspicious links, and receive cyber safety tips via a simple WhatsApp-style interface.

##  Features

- ** Suspicious Link Checker**: Analyze URLs for phishing risks using a local ML model.
- ** Scam Message Detector**: Detect scam texts (OTP fraud, fake jobs, etc.) using NLP.
- ** Multi-Language Support**: Available in English, Hindi, Urdu, Maithili, and Bhojpuri.
- ** Daily Cyber Tips**: Get safety advice in your preferred language.
- ** AI Assistant**: Ask questions about cyber safety (powered by Cohere, optional).
- ** Helpline & Reporting**: Quick access to 1930 and cybercrime.gov.in.

##  Tech Stack

- **Backend**: Python, Flask
- **ML/AI**: Scikit-learn, Pandas, TfidfVectorizer, Logistic Regression
- **NLP**: Cohere (Optional for generative AI)
- **Frontend**: HTML/CSS (Web Chat UI), WhatsApp (Future Integration)

##  Project Structure

```
SafeSathi/
├── app/
│   ├── ai/                 # AI & ML components
│   │   ├── local_models/   # Trained models & feature extraction
│   │   ├── cohere_gpt.py   # Cohere API integration
│   │   └── generative.py   # Explanation logic
│   ├── data/               # Datasets (CSV)
│   ├── templates/          # HTML templates
│   ├── tools/              # Training scripts
│   ├── routes.py           # Flask routes & Webhook
│   ├── utils.py            # Core chatbot logic
│   ├── texts.py            # Multi-language text strings
│   ├── logs.py             # Interaction logging
│   └── __init__.py         # App factory
├── run.py                  # Entry point
├── requirements.txt        # Dependencies
└── README.md               # Documentation
```

##  Setup & Installation

1.  **Clone the repository**:
    ```bash
    git clone <repo-url>
    cd SafeSathi
    ```

2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Train the Models** (Required for first run):
    ```bash
    python app/tools/train_url_model.py
    python app/tools/train_text_model.py
    ```

5.  **Configure Environment**:
    Create a `.env` file in the root directory:
    ```ini
    USE_COHERE=false
    COHERE_API_KEY=your_api_key_here
    SECRET_KEY=your_secret_key
    ```

6.  **Run the Application**:
    ```bash
    python run.py
    ```
    Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

##  Architecture

```mermaid
graph TD
    User[User (WhatsApp/Web)] -->|Message| Flask[Flask Backend]
    Flask -->|Input| Handler[handle_user_input]
    
    Handler -->|Check Link| URLModel[URL Classifier (ML)]
    Handler -->|Check Text| TextModel[Scam Text Classifier (ML)]
    Handler -->|Ask Question| AI[Cohere API / Local Fallback]
    Handler -->|Get Info| Static[Static Content (Tips, Helpline)]
    
    URLModel -->|Result| Response
    TextModel -->|Result| Response
    AI -->|Reply| Response
    Static -->|Text| Response
    
    Response -->|Reply| User
```

##  WhatsApp Integration

The project includes a webhook endpoint at `/webhook/whatsapp` designed to receive POST requests from WhatsApp Business API providers (like Gupshup or Twilio).

**Payload Format (Mock):**
```json
{
  "sender": "919876543210",
  "message": "Is this link safe? http://suspicious-link.com"
}
```

##  Contributing

1. Fork the repo
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

---


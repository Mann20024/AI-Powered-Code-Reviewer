# 🚀 AI-Powered Code Reviewer

An automated code analysis tool designed to streamline the peer-review process. This assistant leverages Large Language Models (LLMs) to identify bugs, suggest performance optimizations, and ensure adherence to clean code standards across multiple programming languages.

## 🌟 Core Features

*   **Automated Logic Validation:** Detects edge cases and potential logical fallacies in code snippets.
*   **Complexity Analysis:** Identifies deeply nested loops or redundant operations that increase time complexity.
*   **Refactoring Suggestions:** Provides actionable advice to improve readability and maintainability.
*   **Multi-Language Support:** Optimized for Python, JavaScript, Java, C++, and Go.
*   **Interactive UI:** Built with Streamlit for a seamless, real-time code review experience.

## 🛠️ Technical Stack

*   **Language:** Python 3.8+
*   **Frontend:** Streamlit
*   **LLM Integration:** OpenAI API (GPT-4)
*   **Libraries:** `openai`, `langchain`, `python-dotenv`

## ⚙️ Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

*   Python 3.8 or higher installed on your machine.
*   An active API key from OpenAI.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YourUsername/ai-code-reviewer.git](https://github.com/YourUsername/ai-code-reviewer.git)
   cd ai-code-reviewer

2. **pip install -r requirements.txt**
3. **Set up Environment Variables:**
   Create a `.env` file in the root directory of the project and add your API key:
   ```env
   OPENAI_API_KEY=your_actual_api_key_here

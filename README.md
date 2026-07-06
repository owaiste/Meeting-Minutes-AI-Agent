# Smart Meeting Minutes & Action Item Tracker 🤖📅

An autonomous concierge AI agent designed to simplify everyday professional and personal organization. This project processes raw, messy conversational meeting transcripts, extracts key decisions, and automatically builds structured action-item tracking tables using the official Google GenAI SDK.

This project was built as a Capstone submission for the **Google Kaggle 5-Day AI Agents Intensive Course (July 2026)** under the **Concierge Agents** track.

## 🚀 Key Features & Applied Course Concepts

This agent demonstrates three core architectural concepts required for graduation:
1. **Official ADK Framework Pattern:** Implements direct initialization and low-temperature configuration using the official `google-genai` client library.
2. **Structured Agent Skills (`SKILL.md`):** Separates system prompt logic from formatting constraints. The agent acts out a custom skill directory layout to ensure standardized Markdown table outputs.
3. **Day 4 Security Guardrails:** Includes a localized programmatic natural language guardrail that actively screens output text to redact placeholders (like "CONFIDENTIAL") and prevent hallucinations.

---

## 🛠️ Project Directory Structure

```text
meeting-agent/
├── .env                  # Private local environment variables (Hidden from GitHub)
├── SKILL.md              # Long-term memory structure and format constraints
├── sample_transcript.txt # Raw conversational transcript input file
├── agent.py              # Main Python agent runtime execution logic
└── README.md             # Project documentation and setup guide
```

---

## ⚡ Setup & Installation Instructions

Follow these steps to run the agent locally on your computer:

### 1. Prerequisites
Ensure you have Python 3.10+ installed on your system. You will also need a verified API Key from **Google AI Studio**.

### 2. Clone and Navigate
```bash
git clone https://github.com
cd meeting-agent
```

### 3. Install Dependencies
Open your terminal or PowerShell and run:
```bash
py -m pip install google-genai python-dotenv
```
*(Use `pip install google-genai python-dotenv` if you are on Mac/Linux).*

### 4. Configure Your Credentials
Create a file named `.env` in the root folder and add your secret API key:
```env
GEMINI_API_KEY=AIzaSyYourActualSecretKeyFromGoogleAIStudio
```
*Note: The `.env` file is excluded from git commits to secure your developer tokens.*

### 5. Run the Agent
Execute the runtime script:
```bash
py agent.py
```

---

## 📊 Sample Agent Output Preview

Upon processing the default raw transcript, the agent applies its markdown skill definitions to instantly output:

### 1. Executive Summary
The team discussed the upcoming launch plan for the new login page, addressing backend readiness and UI design revisions.

### 2. Key Decisions Made
* The core authentication API is confirmed stable.
* A follow-up alignment meeting is locked for Thursday.

### 3. Action Item Tracker

| Task | Owner | Deadline |
| :--- | :--- | :--- |
| Finish database migration script | Sarah | Wednesday afternoon |
| Update Figma error state colors | Ben | Tomorrow morning |
| Draft external release notes | Alex | Post-migration (Wednesday) |

---

## 📄 License
This project is licensed under the **Creative Commons Attribution 4.0 International (CC-BY 4.0)** Open Source Initiative-approved license as mandated by the Kaggle Competition Host Rules.

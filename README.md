# Elderly Companionship Chatbot

## Project Description

This project is a desktop application designed to provide companionship to elderly users through interaction with an AI chatbot. The application features a user-friendly interface and ensures safe and appropriate conversations.

## Key Features

* **Functional Desktop Application:** A complete and runnable Python application with a graphical user interface (GUI).
* **User-Friendly Interface:**
    * Clear and readable font sizes.
    * Customizable background colors.
    * Straightforward layout for easy navigation.
* **Secure User Authentication:** A system for users to register and log in securely.
* **Natural Language Conversation:** The ability to communicate with the chatbot using natural language.
* **Safe and Appropriate Interaction:** The chatbot avoids providing medical or financial advice.
* **Conversation History:**
    * View previous messages within the current chat session.
    * View past conversation history from previous sessions.
* **Personalized Experience**: The chatbot uses the user's name during the conversation.
* **Robust Error Handling:** The application handles common errors gracefully.
* **Local Data Storage:** User data and conversation history are stored locally using an SQLite database.
* **Maintainability and Extensibility:** A modular architecture for easy maintenance and future feature additions.

## Technologies Used

* Python
* Tkinter (GUI)
* SQLite (Local Database)
* Google Generative AI (Gemini)

## Getting Started

1.  **Prerequisites**
    * Python 3.x
    * Google API Key
    * Libraries:  Tkinter, SQLite, google.generativeai, PIL

2.  **Installation**
    * Clone the repository.
    * Install the required libraries.
    * Configure the Google API Key.
    * Set up the SQLite database.

3.  **Usage**
    * Run the main application file.
    * Register a new user or log in.
    * Interact with the chatbot.
    * Customize settings as needed.

## Project Status

The project is complete and functional.

## Future Enhancements

* Further personalization of chatbot responses based on user preferences.
* Additional UI improvements.
* Expanded error handling and logging.

# Setting Up Your Google API Key

This project requires a Google API Key to interact with the Gemini language model. **It is crucial that you do NOT hardcode your API key directly into the code or commit it to version control (like Git).** Instead, you should store it securely as an environment variable.

Follow these steps to generate your API key and set it up:

---

### Step 1: Create or Select a Google Cloud Project

1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  If you don't have a project, you'll be prompted to create one. Follow the on-screen instructions.
3.  If you have existing projects, select the project you wish to use from the project dropdown at the top of the page.

---

### Step 2: Enable the Generative Language API

1.  In the Google Cloud Console, navigate to the **"APIs & Services"** section from the left-hand navigation menu.
2.  Click on **"Library"**.
3.  In the search bar, type "Generative Language API" and press Enter.
4.  Click on the "Generative Language API" from the search results.
5.  Click the **"Enable"** button. Wait a moment for the API to be enabled.

---

### Step 3: Create an API Key

1.  After enabling the API, go back to the **"APIs & Services"** section in the left-hand navigation menu.
2.  Click on **"Credentials"**.
3.  Click the **"+ CREATE CREDENTIALS"** button at the top of the page.
4.  From the dropdown menu, select **"API key"**.
5.  A dialog box will appear displaying your newly generated API key.
6.  **Copy this API key immediately.** This is the only time you'll see the full key.

---

### Step 4: Restrict Your API Key (Recommended for Security)

It's highly recommended to restrict your API key to prevent unauthorized use.

1.  In the "API key created" dialog box, click on **"RESTRICT KEY"**. (If you closed it, you can find your key listed on the "Credentials" page and click its name to edit it).
2.  Under **"Application restrictions"**, for a local desktop application like this, you can initially select "None". However, for more robust applications, you might consider "IP addresses" or "HTTP referrers" if you plan to deploy it in a web context.
3.  Under **"API restrictions"**:
    * Select the **"Restrict key"** radio button.
    * From the "Select APIs" dropdown, choose **"Generative Language API"**. This ensures your key can only be used for this specific API.
4.  Click **"SAVE"**.

---

### Step 5: Set the Environment Variable `GOOGLE_API_KEY`

Now, you need to set this copied API key as an environment variable on your computer.

#### For Windows:

1.  **Search:** Type "environment variables" in the Windows search bar and select "Edit the system environment variables."
2.  **Open Dialog:** In the "System Properties" window, click the "Environment Variables..." button.
3.  **New System Variable:** In the "Environment Variables" dialog, under the "System variables" section (usually the bottom half), click "New...".
4.  **Enter Details:**
    * For "Variable name:", enter `GOOGLE_API_KEY`
    * For "Variable value:", paste your copied API key.
5.  **Confirm:** Click "OK" on all open dialogs to save the changes.
6.  **Restart Terminal:** Close and reopen any Command Prompt or PowerShell windows you are using for your Python project for the changes to take effect.

#### For macOS and Linux:

1.  **Open Terminal:** Open your terminal application.
2.  **Edit Shell Configuration:** You need to add the variable to your shell's configuration file. This is usually `~/.bashrc`, `~/.zshrc`, or `~/.profile`, depending on your shell.
    * For Bash (common default): `nano ~/.bashrc` or `vim ~/.bashrc`
    * For Zsh (common on newer macOS): `nano ~/.zshrc` or `vim ~/.zshrc`
3.  **Add Line:** At the end of the file, add the following line (replace `YOUR_API_KEY_HERE` with your actual key):
    ```bash
    export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```
4.  **Save and Exit:**
    * If using `nano`: Press `Ctrl+X`, then `Y` to confirm save, then `Enter`.
    * If using `vim`: Press `Esc`, then type `:wq`, then `Enter`.
5.  **Apply Changes:** Run the following command to load the updated configuration:
    ```bash
    source ~/.bashrc   # Or source ~/.zshrc, depending on what you edited
    ```
6.  **Verify (Optional):** You can verify by typing `echo $GOOGLE_API_KEY` in your terminal. It should print your API key.

---

Once the environment variable is set, your Python application will be able to access your API key securely.
## Credits

* Krish Jain, Rishika Singh, Kriti Gupta

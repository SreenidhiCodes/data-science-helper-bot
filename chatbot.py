{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMk5jgLzvDEzb0aINfxX8Il",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SreenidhiCodes/data-science-helper-bot/blob/main/chatbot.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Intelligent Data Science Helper Bot\n",
        "\n",
        "print(\" Hello! I am your Data Science Helper Bot.\")\n",
        "print(\"Ask me about datasets, EDA, predictive modeling, or other data science topics.\")\n",
        "print(\"Type 'bye' to exit.\\n\")\n",
        "\n",
        "while True:\n",
        "    user_input = input(\"You: \").lower().strip()\n",
        "\n",
        "    # Exit condition\n",
        "    if \"bye\" in user_input or \"exit\" in user_input:\n",
        "        print(\"Bot: Goodbye! Happy coding! \")\n",
        "        break\n",
        "\n",
        "    # Greetings\n",
        "    elif any(word in user_input for word in [\"hi\", \"hello\", \"hey\", \"good morning\", \"good evening\"]):\n",
        "        print(\"Bot: Hi there! Ready to explore the world of data?\")\n",
        "\n",
        "    # Politeness detection\n",
        "    elif any(word in user_input for word in [\"thank\", \"thanks\", \"thank you\"]):\n",
        "        print(\"Bot: You're welcome!  Glad I could help.\")\n",
        "\n",
        "    # Dataset info\n",
        "    elif \"dataset\" in user_input or \"data set\" in user_input:\n",
        "        print(\"\"\"Bot:  Datasets are collections of data.\n",
        "You can get datasets from:\n",
        "1. Kaggle\n",
        "2. UCI Machine Learning Repository\n",
        "3. Google Dataset Search\n",
        "4. Your own collected data\n",
        "Tip: Always check for missing values & data types before analysis!\"\"\")\n",
        "\n",
        "    # EDA tools\n",
        "    elif \"eda\" in user_input or \"exploratory\" in user_input:\n",
        "        print(\"\"\"Bot:  EDA (Exploratory Data Analysis) Tools:\n",
        "- Pandas & NumPy (Data manipulation)\n",
        "- Matplotlib & Seaborn (Visualizations)\n",
        "- Pandas Profiling / ydata-profiling (Automated EDA reports)\n",
        "- Sweetviz (Quick HTML insights)\n",
        "- DTale (Interactive data browsing)\"\"\")\n",
        "\n",
        "    # Predictive modeling tools\n",
        "    elif \"predictive modeling\" in user_input or \"machine learning\" in user_input or \"ml tools\" in user_input:\n",
        "        print(\"\"\"Bot:  Predictive Modeling Tools:\n",
        "- Scikit-learn (Classic ML algorithms)\n",
        "- XGBoost / LightGBM / CatBoost (Boosting methods)\n",
        "- TensorFlow / PyTorch (Deep learning)\n",
        "Tip: Always start with a baseline model before tuning parameters.\"\"\")\n",
        "\n",
        "    # Feature engineering\n",
        "    elif \"feature engineering\" in user_input or \"feature creation\" in user_input:\n",
        "        print(\"\"\"Bot:  Feature Engineering Tips:\n",
        "- Handle missing values (impute or drop)\n",
        "- Encode categorical variables (One-Hot, Label Encoding)\n",
        "- Scale numerical features (StandardScaler, MinMaxScaler)\n",
        "- Create new features from existing ones (ratios, sums, interactions)\"\"\")\n",
        "\n",
        "    # Model evaluation\n",
        "    elif \"model evaluation\" in user_input or \"evaluate model\" in user_input:\n",
        "        print(\"\"\"Bot:  Model Evaluation Metrics:\n",
        "- Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC\n",
        "- Regression: MAE, MSE, RMSE, R²\n",
        "Tip: Always use cross-validation to avoid overfitting.\"\"\")\n",
        "\n",
        "    # Default fallback\n",
        "    else:\n",
        "        print(\"Bot: Hmm  I’m not sure about that. I can help with datasets, EDA, predictive modeling, feature engineering, and model evaluation.\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mp0j6UeMz9A-",
        "outputId": "2e79950a-dd4e-4e61-c606-ef57d1efae08"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " Hello! I am your Data Science Helper Bot.\n",
            "Ask me about datasets, EDA, predictive modeling, or other data science topics.\n",
            "Type 'bye' to exit.\n",
            "\n",
            "You: HI\n",
            "Bot: Hi there! Ready to explore the world of data?\n",
            "You: WHAT IS EDA\n",
            "Bot:  EDA (Exploratory Data Analysis) Tools:\n",
            "- Pandas & NumPy (Data manipulation)\n",
            "- Matplotlib & Seaborn (Visualizations)\n",
            "- Pandas Profiling / ydata-profiling (Automated EDA reports)\n",
            "- Sweetviz (Quick HTML insights)\n",
            "- DTale (Interactive data browsing)\n",
            "You: THANK YOU\n",
            "Bot: You're welcome!  Glad I could help.\n",
            "You: BYE\n",
            "Bot: Goodbye! Happy coding! \n"
          ]
        }
      ]
    }
  ]
}
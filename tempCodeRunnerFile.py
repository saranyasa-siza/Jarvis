            # if(text.lower()=="jarvis"):
            #     speak("Ya")
            #     # Listen for the command
            #     with sr.Microphone() as source:
            #         print("Jarvis Activated. Listening for command… 🎧")
            #         # recognizer.adjust_for_ambient_noise(source, duration=1)
            #         audio = r.listen(source)

# engine.setProperty('rate', 170)
# engine.setProperty('volume', 1.0)

    # elif "news" in c.lower():
    #     try:
    #         response = requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=2d37fadd71a14e7b868c8471db94e412")
    #         data = response.json()  # converts to dictionary
    #         titles = [article["title"] for article in data["articles"] if article.get("title")]

    #         if titles:
    #             speak("Here are the top news headlines from BBC News.")
    #             for i, title in enumerate(titles[:5], start=1):
    #                 print(f"{i}. {title}")
    #                 speak(f"Headline {i}: {title}")
    #                 time.sleep(1)
    #         else:
    #             speak("Sorry, I couldn't find any news headlines right now.")
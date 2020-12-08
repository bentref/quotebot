from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
session = WolframLanguageSession()


def bad_vibe(message):
    if session.evaluate(wl.Classify("Sentiment", message)) == "Negative":
        return True
    else:
        return False

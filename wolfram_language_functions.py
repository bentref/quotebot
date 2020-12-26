from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, Global, wlexpr
import re
session = WolframLanguageSession()


def bad_vibe(message):
    if session.evaluate(wl.Classify("Sentiment", message)) == "Negative":
        return True
    else:
        return False


def predict_next_word(database, user, phrase):
    messages_list = []
    phrase_list = re.findall(r'\w+', phrase)
    return session.evaluate(wl.SequencePredict(messages_list)(phrase_list))


# def predict_finished_phrase(database, user, phrase, length_remaining):
#     for i in range(length_remaining):
#         phrase.append(predict_next_word(database, user, phrase))
#     return " ".join(phrase)

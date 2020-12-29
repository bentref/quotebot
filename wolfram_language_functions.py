from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl
session = WolframLanguageSession()


def bad_vibe(message):
    if session.evaluate(wl.Classify("Sentiment", message)) == "Negative":
        return True
    else:
        return False


def predict_next_word(database, user, phrase, probabilities=False, num_probs=3):
    messages_list = [wl.TextWords(message) for message in database[user]]
    phrase_list = wl.TextWords(phrase)
    if probabilities:
        predictions = wl.SequencePredict(messages_list)(phrase_list, "Probabilities")
        return session.evaluate(wl.Take(wl.Reverse(wl.Sort(predictions)), num_probs))
    else:
        return session.evaluate(wl.SequencePredict(messages_list)(phrase_list))


# def predict_finished_phrase(database, user, phrase, length_remaining):
#     for i in range(length_remaining):
#         phrase.append(predict_next_word(database, user, phrase))
#     return " ".join(phrase)

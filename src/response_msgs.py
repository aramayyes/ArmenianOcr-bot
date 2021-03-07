from aiogram.utils.emoji import emojize


class ResponseMsgs:
    """Holds all messages that are sent to user by bot."""

    HELP = emojize("Ուղարկեք տեքստ պարունակող նկար, և ես կփոխակերպեմ այն տեքստային տարբերակի: :sunglasses:")
    CONTACT = "Առաջարկների կամ խնդիրների դեպքում կարող եք կապ հաստատել հեղինակի հետ, հետևյալ հասցեով՝ " \
              "aramayis.amiraghyan@yandex.com "

    EMPTY_PHOTO = emojize("Չհաջողվեց նկարում տեքստ գտնել: :pensive:")
    INTERNAL_ERROR = emojize(
        "Ինչ-որ բան այն չէ, ներեցեք: :disappointed: :disappointed: Փորձեք մի փոքր ուշ:")

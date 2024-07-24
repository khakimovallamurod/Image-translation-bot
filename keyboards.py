from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from db import get_models, get_one_model

def home_keyboard():
    return ReplyKeyboardMarkup(
        [
            [KeyboardButton('🛍 Toplamlar'), KeyboardButton('☎️Contact')],
        ],
        resize_keyboard=True,
    )

def models_keyboard():
    btns = []
    for model in get_models():
        btns.append([InlineKeyboardButton(model, callback_data=f'model:{model}')])
    return InlineKeyboardMarkup(
        btns,
        resize_keyboard=True
    )

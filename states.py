from aiogram.fsm.state import State, StatesGroup

class ContactForm(StatesGroup):
    waiting_for_message = State()
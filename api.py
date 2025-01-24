
import random
import asyncio
import openai
from hw_27_data import DATA

openai.api_key = "sk-or-vv-3ebcec4c76b91fc5aae7cc6f3367592f42b4f634f96d1b1572e32d07a63b579e"
openai.api_base = "https://api.vsegpt.ru/v1"

MAX_CHUNK_SIZE = 2000
SLEEP_TIME = 1

PROMPT_CONSPECT_WRITER = """
Привет!
Ты опытный технический писатель. Ниже, я предоставляю тебе полный текст лекции, а так же ту часть,
с которой ты будешь работать.

Ты великолепно знаешь русский язык и отлично владеешь этой темой.

Тема занятия: {topic}

Полный текст лекции:
{full_text}

Сейчас я дам тебе ту часть, с которой ты будешь работать. Я попрошу тебя написать конспект лекции
и добавить блоки кода, если необходимо.

Ты пишешь в формате Markdown. Начни с заголовка 2го уровня.
В тексте используй заголовки 3го уровня.

Используй блоки кода по необходимости.

Отрезок текста, с которым ты работаешь:
{text_to_work}
"""

def split_text(text: str, max_chunk_size: int = MAX_CHUNK_SIZE) -> list:
    ...

async def get_ai_request(...):
    ...

def save_to_markdown(...):
    ...

async def main():
    """
    1) Собираем полный текст (из всех элементов DATA).
    2) Выбираем 20 случайных (или 5 для теста).
    """
    topic = "Пример использования Bootstrap"

    full_text = "\n".join([item["text"] for item in DATA])

    #Указываем количество случайных запросов из файла
    selected_fragments = random.sample(DATA, 7)

    for idx, d in enumerate(selected_fragments, start=1):
        fragment_text = d["text"]
        prompt = PROMPT_CONSPECT_WRITER.format(
            topic=topic,
            full_text=full_text,
            text_to_work=fragment_text
        )
        print(f"[DEBUG] Prompt for fragment #{idx} ready.")
        

    print("Часть main() готова к тестам!")

if __name__ == "__main__":
    asyncio.run(main())

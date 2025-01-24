# async_vsegpt_client_part1.py

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
    """
    Разбивает текст на части (чанки) не более max_chunk_size символов,
    стараясь не обрывать слова.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chunk_size
        if end < len(text):
            space_pos = text.rfind(" ", start, end)
            if space_pos == -1:
                space_pos = end
            chunk = text[start:space_pos]
            start = space_pos
        else:
            chunk = text[start:]
            start = len(text)

        chunk = chunk.strip()
        if chunk:
            chunks.append(chunk)

    return chunks

async def get_ai_request(
    prompt: str,
    model: str = "openai/gpt-4o-mini",
    max_tokens: int = 16000,
    temperature: float = 0.7
) -> str:
    """
    Асинхронный запрос к API VseGPT/OpenAI, возвращаем ответ строки.
    """
    try:
        response = await openai.ChatCompletion.acreate(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Ошибка при запросе: {e}"

def save_to_markdown(results: list, filename: str = "final_conspect.md") -> None:
    """
    Сохраняет результаты в один Markdown-файл, используя разделители '---'.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Итоговый конспект\n\n")
        for i, content in enumerate(results, start=1):
            f.write("---\n")
            f.write(f"## Фрагмент {i}\n\n")
            f.write(content)
            f.write("\n\n")

# Пока main() сделаем заглушкой:
async def main():
    pass

if __name__ == "__main__":
    asyncio.run(main())

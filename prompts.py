from langchain_core.prompts import ChatPromptTemplate

# Шаг 1: Анализ задачи
ANALYZE_PROMPT = ChatPromptTemplate.from_template(
    "Ты аналитик. Разбери задачу по пунктам: требования, входы/выходы, "
    "граничные случаи. Кратко, списком.\n\nЗадача: {task}"
)

# Шаг 2: Подбор инструментов (видит анализ)
TOOLS_PROMPT = ChatPromptTemplate.from_template(
    "На основе анализа задачи подбери инструменты: стандартная библиотека "
    "или внешние пакеты. Обоснуй выбор одной строкой на инструмент.\n\n"
    "Задача: {task}\n\nАнализ:\n{analysis}"
)

# Шаг 3: Реализация (видит анализ + инструменты)
CODE_PROMPT = ChatPromptTemplate.from_template(
    "Напиши код на Python по задаче, используя выбранные инструменты. "
    "Только код, без markdown.\n\n"
    "Задача: {task}\n\nАнализ:\n{analysis}\n\nИнструменты:\n{tools}"
)

# Шаг 4: Ревью (видит задачу + код)
REVIEW_PROMPT = ChatPromptTemplate.from_template(
    "Ты ревьюер. Проверь код: корректность, граничные случаи, стиль. "
    "Дай вердикт (OK / нужны правки) и список замечаний.\n\n"
    "Задача: {task}\n\nКод:\n{code}"
)
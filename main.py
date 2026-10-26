from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from prompts import ANALYZE_PROMPT, TOOLS_PROMPT, CODE_PROMPT, REVIEW_PROMPT

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
parser = StrOutputParser()

# Цепочки по шагам
analyze_chain = ANALYZE_PROMPT | llm | parser
tools_chain   = TOOLS_PROMPT   | llm | parser
code_chain    = CODE_PROMPT    | llm | parser
review_chain  = REVIEW_PROMPT  | llm | parser

# Сборка пайплайна: накапливаем поля в словаре
pipeline = (
    RunnablePassthrough.assign(analysis=analyze_chain)
    | RunnablePassthrough.assign(tools=tools_chain)
    | RunnablePassthrough.assign(code=code_chain)
    | RunnablePassthrough.assign(review=review_chain)
)

def run(task: str) -> dict:
    """Прогоняет задачу через все четыре шага и возвращает результат."""
    return pipeline.invoke({"task": task})

if __name__ == "__main__":
    task = input("Введите задачу для генерации кода: ").strip()
    if not task:
        print("Задача не введена, выходим.")
        raise SystemExit(1)

    result = run(task)


    print("=== АНАЛИЗ ===\n", result["analysis"])
    print("\n=== ИНСТРУМЕНТЫ ===\n", result["tools"])
    print("\n=== КОД ===\n", result["code"])
    print("\n=== РЕВЬЮ ===\n", result["review"])
import ast
import sys
from pathlib import Path


def audit_file(filepath):
    path = Path(filepath)

    if not path.exists():
        print(f"[ERROR] Файл не найден: {filepath}")
        return 1

    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as error:
        print(f"[ERROR] Ошибка в коде: строка {error.lineno}")
        return 1

    found = False

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            length = (node.end_lineno or node.lineno) - node.lineno + 1

            if length > 25:
                print(f"[LENGTH] Строка {node.lineno}: функция {node.name} длинная ({length} строк)")
                found = True

            if node.returns is None:
                print(f"[TYPE] Строка {node.lineno}: у функции {node.name} нет аннотации возврата")
                found = True

        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "print":
            print(f"[PRINT] Строка {node.lineno}: найден print()")
            found = True

    if not found:
        print("Проблем не найдено.")

    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python check_complexity.py <путь_к_файлу>")
        sys.exit(1)


    sys.exit(audit_file(sys.argv[1]))

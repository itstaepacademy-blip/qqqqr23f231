# Legacy audit — заготовка лабораторной


## Проверка файла

Из корня проекта запусти:

```bash
python .github/skills/legacy-audit/scripts/check_complexity.py src/legacy_processor.py
```

Скрипт проверяет длинные функции (больше 25 строк), отсутствие аннотации возврата и вызовы `print()`.

## Проверки проекта

```bash
ruff check .
pytest
```

Перед рефакторингом сначала посмотри отчёт аудита и согласуй изменения.

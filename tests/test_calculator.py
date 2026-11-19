from Linus.LinusTA import Calculator


def press_keys(calculator: Calculator, keys: str) -> str:
    for key in keys.split():
        calculator.press(key)
    return calculator.display


def test_chained_operations_and_repeat_equals() -> None:
    calculator = Calculator()

    assert press_keys(calculator, "8 + 2 × 3 =") == "30"
    assert calculator.press("=") is None
    assert calculator.display == "90"


def test_decimal_percent_and_sign() -> None:
    calculator = Calculator()

    assert press_keys(calculator, "1 2 . 5 % +/−") == "-0.125"


def test_percent_of_first_operand_for_addition() -> None:
    calculator = Calculator()

    assert press_keys(calculator, "2 0 0 + 1 0 % =") == "220"


def test_division_by_zero_shows_error_and_recovers() -> None:
    calculator = Calculator()

    assert press_keys(calculator, "8 ÷ 0 =") == "Fehler"
    assert calculator.press("7") is None
    assert calculator.display == "7"


def test_clear_resets_pending_operation() -> None:
    calculator = Calculator()

    assert press_keys(calculator, "9 + AC 2 =") == "2"

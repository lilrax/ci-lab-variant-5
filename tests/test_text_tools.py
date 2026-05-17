from ci_lab.text_tools import normalize_text, unique_words, word_count


def test_normalize_text_removes_extra_spaces_and_lowers_case() -> None:
    assert normalize_text("  Hello   WORLD  ") == "hello world"

def test_word_count_counts_words() -> None:
    assert word_count("Python CI with GitHub Actions") == 5

def test_word_count_returns_zero_for_empty_text() -> None:
    assert word_count("   ") == 0

def test_unique_words_returns_only_unique_values() -> None:
    assert unique_words("Python python CI") == {"python", "ci"}

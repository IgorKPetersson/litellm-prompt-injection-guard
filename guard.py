import re


INJECTION_PATTERNS = [
    r"ignore (all|any|the|your)? ?previous instructions",
    r"ignore .* instructions",
    r"disregard .* instructions",
    r"forget .* instructions",
    r"reveal .* system prompt",
    r"show .* system prompt",
    r"print .* system prompt",
    r"what is your system prompt",
    r"developer message",
    r"act as if .* no restrictions",
]


def detect_prompt_injection(prompt: str) -> tuple[bool, str]:
    """
    Detect simple prompt-injection attempts using rule-based patterns.

    Returns:
        (True, reason) if suspicious input is detected.
        (False, "") if the input is allowed.
    """

    normalized_prompt = prompt.lower().strip()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, normalized_prompt):
            return True, f"Matched suspicious pattern: {pattern}"

    return False, ""
# u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8: Funniest One-Line Out-of-Office Reply
# One funny out-of-office email auto-reply, one line long.
# The program writes the reply to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
REPLY = "I'm out of office until Monday. My inbox is now handled by my houseplant, which has already filed for overtime."


def validate_reply(text):
    assert 1 <= len(text) <= 160, "reply must be 1-160 characters"
    assert text.strip(), "reply must not be only whitespace"
    assert "\n" not in text, "reply must be a single line"


def main():
    validate_reply(REPLY)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()

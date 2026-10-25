"""检查本仓库使用的内联 Markdown 链接、锚点和题目索引；仅使用标准库。"""

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]\n]+)\]\(([^\s)]+)\)")
QUESTION = re.compile(r"^### ([A-Z]\d{2})｜(.+?)【(P[01])】$", re.MULTILINE)
EXPLICIT_ANCHOR = re.compile(r'<a\s+id="([^"]+)"\s*></a>')
FENCE = re.compile(r"^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", re.MULTILINE | re.DOTALL)


def prose(text):
    text = FENCE.sub("", text)
    return re.sub(r"`[^`\n]+`", "", text)


def anchors(text):
    result = set(EXPLICIT_ANCHOR.findall(text))
    counts = Counter()
    for title in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\s-]", "", title.lower()).replace(" ", "-")
        count = counts[slug]
        result.add("{}-{}".format(slug, count) if count else slug)
        counts[slug] += 1
    return result


def main():
    paths = [
        path for path in ROOT.rglob("*.md")
        if not any(part in {".git", ".venv", "venv", "node_modules"} for part in path.relative_to(ROOT).parts)
    ]
    documents = {path.resolve(): prose(path.read_text(encoding="utf-8")) for path in paths}
    anchor_map = {path: anchors(text) for path, text in documents.items()}
    errors = []
    link_count = 0
    questions = {}
    for path, text in documents.items():
        relative = path.relative_to(ROOT)
        for anchor, count in Counter(EXPLICIT_ANCHOR.findall(text)).items():
            if count > 1:
                errors.append("{}: duplicate anchor {}".format(relative, anchor))
        for label, href in LINK.findall(text):
            url = urlsplit(href.strip("<>"))
            if url.scheme or url.netloc:
                continue
            link_count += 1
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.exists():
                errors.append("{}: missing target {}".format(relative, href))
            elif url.fragment and target.suffix == ".md":
                if unquote(url.fragment) not in anchor_map.get(target, set()):
                    errors.append("{}: missing anchor {}".format(relative, href))
        if re.match(r"\d{2}-", path.name):
            for question_id, title, priority in QUESTION.findall(text):
                if question_id in questions:
                    errors.append("duplicate question ID: {}".format(question_id))
                questions[question_id] = "{}#{}".format(path.name, question_id.lower())
                if question_id.lower() not in EXPLICIT_ANCHOR.findall(text):
                    errors.append("{}: missing explicit question anchor {}".format(relative, question_id))

    index = documents.get((ROOT / "docs/question-bank.md").resolve(), "")
    index_entries = [(label, href) for label, href in LINK.findall(index) if re.fullmatch(r"[A-Z]\d{2}", label)]
    indexed = Counter(label for label, href in index_entries)
    for question_id, expected_href in questions.items():
        if indexed[question_id] != 1:
            errors.append("{}: expected one question-bank entry".format(question_id))
    for question_id, href in index_entries:
        if questions.get(question_id) != href:
            errors.append("{}: incorrect or unknown index target {}".format(question_id, href))

    readme = documents.get((ROOT / "README.md").resolve(), "")
    advertised = re.search(r"\[(\d+) 道面试题索引\]", readme)
    if not advertised or int(advertised.group(1)) != len(questions):
        errors.append("README question count does not match chapter questions")
    if not questions:
        errors.append("no chapter questions found")
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    print("Checked {} Markdown files, {} local links, and {} indexed questions.".format(
        len(documents), link_count, len(questions)
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())

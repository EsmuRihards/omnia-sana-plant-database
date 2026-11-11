"""Section-level YAML editing for plant records: only the top-level sections you
change are re-serialised; every other byte of the file is left untouched (a full
yaml.safe_dump reflows hand-quoted strings such as harvest_readiness)."""
import re
import yaml

TOP = re.compile(r'(?m)^([A-Za-z_][A-Za-z0-9_]*):')


def split_sections(text):
    """[(key, chunk)] in file order; chunk runs from its key line to the next top-level key."""
    marks = [(m.start(), m.group(1)) for m in TOP.finditer(text)]
    out = []
    for n, (pos, key) in enumerate(marks):
        end = marks[n + 1][0] if n + 1 < len(marks) else len(text)
        out.append((key, text[pos:end]))
    head = text[:marks[0][0]] if marks else text
    return head, out


def dump_section(key, value):
    return yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True, width=100)


def load(path):
    text = open(path, encoding='utf-8', newline='').read()
    return text, yaml.safe_load(text)


def save(path, text, data, changed_keys):
    """Rewrite only `changed_keys`; keys absent from `data` are deleted, new keys appended."""
    head, secs = split_sections(text)
    seen = set()
    parts = [head]
    for key, chunk in secs:
        seen.add(key)
        if key in changed_keys:
            if key in data:
                parts.append(dump_section(key, data[key]))
        else:
            parts.append(chunk)
    for key in changed_keys:
        if key not in seen and key in data:
            if parts and not parts[-1].endswith('\n'):
                parts[-1] += '\n'  # last section had no trailing newline
            parts.append(dump_section(key, data[key]))
    new = ''.join(parts)
    assert yaml.safe_load(new) == data, 'splice changed data outside the edited sections'
    open(path, 'w', encoding='utf-8', newline='').write(new)
    return new

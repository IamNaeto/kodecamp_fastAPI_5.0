def format_section(title, content, underline_char="-"):
    return f"\n{title}\n{underline_char * len(title)}\n{content}"

def format_list(title, items):
    body = "\n".join(f"- {item}" for item in items)
    return format_section(title, body)

def format_experience(experiences):
    lines = []
    for job in experiences:
        header = f"{job['position']} at {job['company']} ({job['years']})"
        details = "\n".join(f"  • {d}" for d in job['details'])
        lines.append(f"{header}\n{details}")
    return format_section("Experience", "\n\n".join(lines))

def format_education(edu):
    content = f"{edu['degree']} — {edu['institution']} ({edu['years']})"
    return format_section("Education", content)

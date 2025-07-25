import json
import os
from formatter import format_section, format_list, format_experience, format_education

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESUME_PATH = os.path.join(BASE_DIR, "resume.json")

def load_resume():
    with open(RESUME_PATH, "r") as f:
        return json.load(f)

def generate_resume(data):
    lines = []
    lines.append(f"{data['name'].upper()}\n{data['title']}")
    contact_info = " | ".join([f"{k.capitalize()}: {v}" for k, v in data['contact'].items()])
    lines.append(contact_info)

    lines.append(format_section("Summary", data['summary']))
    lines.append(format_list("Skills", data['skills']))
    lines.append(format_experience(data['experience']))
    lines.append(format_education(data['education']))

    return "\n".join(lines)

def save_resume(text, format_type="txt"):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(BASE_DIR, f"output_resume.{format_type}")
    with open(filename, "w") as f:
        f.write(text)
    print(f"Resume saved as {filename}")

def main():
    data = load_resume()
    resume_text = generate_resume(data)

    print("\n=== Generated Resume ===\n")
    print(resume_text)

    save_resume(resume_text, "txt")
    save_resume(resume_text, "md")

if __name__ == "__main__":
    main()

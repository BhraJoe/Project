import os

def fix_styles_case(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace 'styles/' with 'Styles/' and '../styles/' with '../Styles/'
                new_content = content.replace('styles/', 'Styles/')
                
                if content != new_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed: {filepath}")

if __name__ == "__main__":
    project_dir = r"c:\Users\Joe\Desktop\New folder (2)\Project"
    fix_styles_case(project_dir)

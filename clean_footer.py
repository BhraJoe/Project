import os

# Directories to search
DIRS = [
    r'c:\Users\Joe\Desktop\New folder (2)\Project',
    r'c:\Users\Joe\Desktop\New folder (2)\Project\yes'
]

TARGET = 'with Premium Redesign'

def update_footers():
    for directory in DIRS:
        for filename in os.listdir(directory):
            if filename.endswith('.html'):
                filepath = os.path.join(directory, filename)
                
                content = None
                # Try different encodings
                for enc in ['utf-8', 'latin-1', 'cp1252']:
                    try:
                        with open(filepath, 'r', encoding=enc) as f:
                            content = f.read()
                        break
                    except:
                        continue
                
                if content and TARGET in content:
                    updated_content = content.replace(TARGET, '')
                    
                    # Clean up double spaces if any
                    updated_content = updated_content.replace('  ', ' ')
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(updated_content)
                    print(f"Updated: {os.path.join(os.path.basename(directory), filename)}")

if __name__ == "__main__":
    update_footers()

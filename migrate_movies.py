import os
import re

# Paths
YES_DIR = r'c:\Users\Joe\Desktop\New folder (2)\Project\yes'
TEMPLATE_PATH = r'c:\Users\Joe\Desktop\New folder (2)\Project\yes\ghostbusters.html'

def get_template_content():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def update_files(target_files=None):
    template_content = get_template_content()
    
    files_to_process = target_files if target_files else os.listdir(YES_DIR)
    
    for filename in files_to_process:
        if not filename.endswith('.html') or filename in ['ghostbusters.html', 'mad max.html', 'warchief.html']:
            continue
            
        filepath = os.path.join(YES_DIR, filename)
        legacy_html = None
        
        # Try different encodings
        for enc in ['utf-8', 'latin-1', 'cp1252', 'utf-16']:
            try:
                with open(filepath, 'r', encoding=enc) as f:
                    legacy_html = f.read()
                break
            except Exception:
                continue
        
        if not legacy_html:
            print(f"Failed to read {filename} with any encoding.")
            continue
            
        try:
            # Extract data
            title_match = re.search(r'<h1 class="thr-1">(.*?)</h1>', legacy_html, re.IGNORECASE)
            title = title_match.group(1).strip() if title_match else filename.replace('.html', '').title()
            
            iframe_match = re.search(r'(<iframe.*?>.*?</iframe>)', legacy_html, re.DOTALL | re.IGNORECASE)
            iframe_str = iframe_match.group(1).strip() if iframe_match else '<p>Trailer coming soon...</p>'
            
            release_match = re.search(r'Release Date:\s*(.*?)</h4', legacy_html, re.IGNORECASE)
            release = release_match.group(1).strip() if release_match else 'TBA'
            
            desc_match = re.search(r'<p class="thr-3">(.*?)</p>', legacy_html, re.DOTALL | re.IGNORECASE)
            description = desc_match.group(1).strip() if desc_match else 'Dive into another world-class cinematic experience from the MovieMax collection.'
            
            new_content = template_content
            new_content = re.sub(r'<title>.*?</title>', f'<title>Watch {title} | MovieMax</title>', new_content)
            new_content = re.sub(r'<h1>Ghostbusters: Frozen Empire</h1>', f'<h1>{title}</h1>', new_content)
            new_content = re.sub(r'<div class="video-wrapper">.*?</div>', f'<div class="video-wrapper">{iframe_str}</div>', new_content, flags=re.DOTALL)
            new_content = re.sub(r'<span>Release:</span> March 22', f'<span>Release:</span> {release}', new_content)
            
            rating = "4." + str(hash(title) % 10)
            new_content = re.sub(r'<span style="color:#fff; font-weight:700;">4.8</span>', f'<span style="color:#fff; font-weight:700;">{rating}</span>', new_content)
            
            desc_pattern = r'<div class="movie-description">.*?</div>'
            new_content = re.sub(desc_pattern, f'<div class="movie-description">{description}</div>', new_content, flags=re.DOTALL)
            
            new_content = re.sub(r'<span class="details-value">Action / Thriller</span>', '<span class="details-value">Cinematic Feature</span>', new_content)
            new_content = re.sub(r'<span class="details-value">Gil Kenan</span>', '<span class="details-value">TBA</span>', new_content)
            
            cast_block = """<div class="cast-list details-value">
                        <span>Lead 1</span>
                        <span>Lead 2</span>
                        <span>Supporting Cast</span>
                    </div>"""
            new_content = re.sub(r'<div class="cast-list details-value">.*?</div>', cast_block, new_content, flags=re.DOTALL)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
            print(f"Success: {filename}")
            
        except Exception as e:
            print(f"Error {filename}: {e}")

if __name__ == "__main__":
    # Process only the ones that failed or everything again to be sure
    update_files(['breaking.html', 'control.html'])

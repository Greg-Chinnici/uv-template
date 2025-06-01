import argparse
import subprocess
from pathlib import Path

# dict for keyword to git repo link
KNOWN_TEMPLATES = {
    
}

def main():
    print("Making Project")
    parser = argparse.ArgumentParser(description='Init a UV project with a specific template')
    parser.add_argument('name' , help='folder/project name')
    parser.add_argument('template', help= 'template keyword or git url' ,nargs="?" , default=None)
    args = parser.parse_args()

    template_url = KNOWN_TEMPLATES.get(args.template , args.template) if args.template else None
    final_dir = Path(args.name)
    print(f"Creating {args.name} at {final_dir}")

    if final_dir.exists():
        print("That Directory Already Exists, choose a different name")
        return 
    
    if template_url:
        subprocess.run(['git' , 'clone' , template_url , args.name], check=True)
        subprocess.run(['uv' , 'venv' , '.venv'], cwd = final_dir, check=True)
        
        requirements = Path.joinpath(final_dir , 'requirements.txt')
        if requirements.exists():
            with open(requirements) as req:
                for line in req:
                    pkg = line.strip()
                    if pkg.startswith('#'): continue
                    subprocess.run(['uv' , 'pip' , 'install' , '--add' , pkg] , cwd = final_dir , check=True)
            requirements.unlink()

        toml = Path.joinpath(final_dir ,  'pyproject.toml')
        if toml.exists():
            subprocess.run(['uv' , 'sync'])

    else:
        subprocess.run(['uv' , 'init' , args.name])

    print("Project Started. START CODING")

if __name__ == '__main__':
    main()

# Development Setup

## Prerequisites

- Python 3.11 or newer
- [pip](https://pip.pypa.io/en/stable/)
- (Recommended) [virtualenv](https://virtualenv.pypa.io/en/latest/) or [venv](https://docs.python.org/3/library/venv.html)

## Setting Up for Development

1. **Clone the repository**  
   ```sh
   git clone git@github.com:jdegeus/flask-template.git
   cd flask-template
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   pip install -r dev-requirements.txt
   ```

4. **Run the app in development mode**  
   ```sh
   python app.py
   ```
   The app will be available at http://127.0.0.1:5000

   **Alternatively, you can use Flask's built-in CLI:**
   ```sh
   flask run
   ```
   By default, the app will be available at http://127.0.0.1:5000

   > **Note:**  
   > When using `flask run`, you must run the command from the directory containing `app.py`,  
   > or set the `FLASK_APP` environment variable to the correct relative or absolute path to your app file.  
   > If your file is named `app.py` and contains `app = Flask(__name__)`, Flask will often detect it automatically.

# Building a Standalone Executable

This project uses [PyInstaller](https://pyinstaller.org/) (included in `dev-requirements.txt`) to create a standalone executable.

1. **Build the executable**  
   ```sh
   pyinstaller app.spec
   ```
   The executable will be created in the `dist/` directory.

2. **Run the built executable**  
   ```sh
   dist/app.exe
   ```

## Notes

- Update `app.spec` if you add new files or dependencies.
- Static files and templates are included via the spec file; ensure they are listed if you add more.
- For troubleshooting PyInstaller builds, check the `build/` directory for logs and warnings.
